"""
lionguard2lite.py
"""

import torch
import torch.nn as nn
from transformers import PretrainedConfig, PreTrainedModel

INPUT_DIMENSION = 768 # EmbeddingGemma-300m input dimensions

CATEGORIES = {
    "binary": ["binary"],
    "hateful": ["hateful_l1", "hateful_l2"],
    "insults": ["insults"],
    "sexual": [
        "sexual_l1",
        "sexual_l2",
    ],
    "physical_violence": ["physical_violence"],
    "self_harm": ["self_harm_l1", "self_harm_l2"],
    "all_other_misconduct": [
        "all_other_misconduct_l1",
        "all_other_misconduct_l2",
    ],
}

CATEGORY_ORDER = [
    "binary",
    "hateful",
    "insults",
    "sexual",
    "physical_violence",
    "self_harm",
    "all_other_misconduct",
]


class LionGuard2LiteConfig(PretrainedConfig):
    model_type = "lionguard2lite"

    def __init__(
        self,
        input_dim=INPUT_DIMENSION,
        categories=CATEGORIES,
        category_order=CATEGORY_ORDER,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.input_dim = input_dim
        self.categories = categories
        self.category_order = category_order


class LionGuard2LiteModel(PreTrainedModel):
    config_class = LionGuard2LiteConfig

    def __init__(self, config: LionGuard2LiteConfig):
        """
        LionGuard2Lite is a localised content moderation model that flags whether text violates the following categories:

        1. `hateful`: Text that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of a protected identity.

        There are two sub-categories for the `hateful` category:
        a. `level_1_discriminatory`: Text that contains derogatory or generalized negative statements targeting a protected group.
        b. `level_2_hate_speech`: Text that explicitly calls for harm or violence against a protected group; or language praising or justifying violence against them.

        2. `insults`: Text that insults demeans, humiliates, mocks, or belittles a person or group **without** referencing a legally protected trait.
        For example, this includes personal attacks on attributes such as someone’s appearance, intellect, behavior, or other non-protected characteristics.

        3. `sexual`: Text that depicts or indicates sexual interest, activity, or arousal, using direct or indirect references to body parts, sexual acts, or physical traits.
        This includes sexual content that may be inappropriate for certain audiences.

        There are two sub-categories for the `sexual` category:
        a. `level_1_not_appropriate_for_minors`: Text that contains mild-to-moderate sexual content that is generally adult-oriented or potentially unsuitable for those under 16.
            May include matter-of-fact discussions about sex, sexuality, or sexual preferences.
        b. `level_2_not_appropriate_for_all_ages`: Text that contains content aimed at adults and considered explicit, graphic, or otherwise inappropriate for a broad audience.
            May include explicit descriptions of sexual acts, detailed sexual fantasies, or highly sexualized content.

        4. `physical_violence`: Text that includes glorification of violence or threats to inflict physical harm or injury on a person, group, or entity.

        5. `self_harm`: Text that promotes, suggests, or expresses intent to self-harm or commit suicide.

        There are two sub-categories for the `self_harm` category:
        a. `level_1_self_harm_intent`: Text that expresses suicidal thoughts or self-harm intention; or content encouraging someone to self-harm.
        b. `level_2_self_harm_action`: Text that describes or indicates ongoing or imminent self-harm behavior.

        6. `all_other_misconduct`: This is a catch-all category for any other unsafe text that does not fit into the other categories.
        It includes text that seeks or provides information about engaging in misconduct, wrongdoing, or criminal activity, or that threatens to harm,
        defraud, or exploit others. This includes facilitating illegal acts (under Singapore law) or other forms of socially harmful activity.

        There are two sub-categories for the `all_other_misconduct` category:
        a. `level_1_not_socially_accepted`: Text that advocates or instructs on unethical/immoral activities that may not necessarily be illegal but are socially condemned.
        b. `level_2_illegal_activities`: Text that seeks or provides instructions to carry out clearly illegal activities or serious wrongdoing; includes credible threats of severe harm.

        Lastly, there is an additional `binary` category (#7) which flags whether the text is unsafe in general.

        The model takes in as input text, after it has been encoded with Google's `embeddinggemma-300m` model.

        The model outputs the probabilities of each category being true.

        ================================

        Args:
            input_dim: The dimension of the input embeddings. This defaults to 768, which is the dimension of the embeddings from Google's `embeddinggemma-300m` model. This should not be changed.
            label_names: The names of the labels. This defaults to the keys of the CATEGORIES dictionary. This should not be changed.
            categories: The categories of the labels. This defaults to the CATEGORIES dictionary. This should not be changed.

        Returns:
            A LionGuard2Lite model.
        """
        super().__init__(config)
        self.input_dim = config.input_dim
        self.categories = config.categories
        self.category_order = config.category_order
        self.n_outputs = len(self.category_order)

        # Shared layers
        self.shared_layers = nn.Sequential(
            nn.Linear(self.input_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
        )

        # Output heads for each label
        self.output_heads = nn.ModuleList(
            [
                nn.Sequential(
                    nn.Linear(128, 32),
                    nn.ReLU(),
                    nn.Linear(32, 2),  # 2 thresholds for ordinal classification
                    nn.Sigmoid(),
                )
                for _ in range(self.n_outputs)
            ]
        )

    def forward(self, x):
        # Pass through shared layers
        h = self.shared_layers(x)
        # Pass through each output head
        return [head(h) for head in self.output_heads]

    def predict(self, embeddings):
        """
        Predict the probabilities of each label being true.

        Args:
            embeddings: A numpy array of embeddings (N * INPUT_DIMENSION)

        Returns:
            A dictionary of probabilities.
        """
        # Convert input to PyTorch tensor if not already
        if not isinstance(embeddings, torch.Tensor):
            x = torch.tensor(embeddings, dtype=torch.float32)
        else:
            x = embeddings

        # Pass through model
        with torch.no_grad():
            outputs = self.forward(x)

        # Stack outputs into a single tensor
        raw_predictions = torch.stack(outputs)  # SIZE:

        # Extract and format probabilities from raw predictions
        output = {}
        for i, main_cat in enumerate(self.category_order):
            sub_categories = self.categories[main_cat]
            for j, sub_cat in enumerate(sub_categories):
                # j=0 uses P(y>0)
                # j=1 uses P(y>1) if L2 category exists
                output[sub_cat] = raw_predictions[i, :, j]

            # Post processing step:
            # If L2 category exists, and P(L2) > P(L1),
            # Set both P(L1) and P(L2) to their average to maintain ordinal consistency
            if len(sub_categories) > 1:
                l1 = output[sub_categories[0]]
                l2 = output[sub_categories[1]]

                # Update probabilities on samples where P(L2) > P(L1)
                mask = l2 > l1
                mean_prob = (l1 + l2) / 2
                l1[mask] = mean_prob[mask]
                l2[mask] = mean_prob[mask]
                output[sub_categories[0]] = l1
                output[sub_categories[1]] = l2

        for key, value in output.items():
            output[key] = value.numpy().tolist()
        return output
