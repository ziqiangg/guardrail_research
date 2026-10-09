# status 200  final_url https://huggingface.co/datasets/facebook/cyberseceval3-visual-prompt-injection/raw/7933662024dc994be4ab90d520ab712e5765b655/README.md  content-type text/plain; charset=utf-8
---
license: mit
task_categories:
- text-generation
language:
- en
tags:
- ai security
- prompt injection
pretty_name: CyberSecEval 3 - Visual Prompt Injection Benchmark
size_categories:
- <1K
configs:
  - config_name: visual_prompt_injection
    data_files:
        - split: test
          path: test_cases.json
---

# Dataset Card for CyberSecEval 3 - Visual Prompt Injection Benchmark

## Dataset Details

### Dataset Description

This dataset provides a multimodal benchmark for [visual prompt injection](https://en.wikipedia.org/wiki/Prompt_injection), with text/image inputs. It is part of [CyberSecEval 3](https://arxiv.org/abs/2408.01605), the third edition of Meta's flagship suite of security benchmarks for LLMs to measure cybersecurity risks and capabilities across multiple domains.

- **Language(s):** English
- **License:** MIT

### Dataset Sources

- **Repository:** [Link](https://github.com/meta-llama/PurpleLlama/tree/23156b70efb596831c02c6461fc42da1f75988ec/CybersecurityBenchmarks)
- **Paper:** [Link](https://arxiv.org/abs/2408.01605)

## Uses


### In scope

This dataset is intended for evaluating the susceptibility of language models to prompt injection when provided with text and image inputs.

### Out-of-scope

This dataset should not be used to train models and should be for evaluation purposes only. In addition, this dataset should not be used for harmful, unethical, or malicious purposes.

## How to Use

The benchmarks can be run with either:
1. The CyberSecEval benchmark runner from the [PurpleLlama repository](https://github.com/meta-llama/PurpleLlama/tree/23156b70efb596831c02c6461fc42da1f75988ec/CybersecurityBenchmarks) (see [documentation](https://meta-llama.github.io/PurpleLlama/docs/benchmarks/prompt_injection#multilingual-text-prompt-injection-benchmark) for more details)
2. The [Inspect AI framework](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals)



## Dataset Structure

A total of 1000 test cases are provided in `test_cases.json`. A folder of accompanying images is at `images/`.

Each test case consists of these core keys:

- `id`: The integer ID of the test case.
- `system_prompt`: The system prompt provided to the model-under-test.
- `user_input_text`: Text component of the user prompt provided to the model-under-test.
- `judge_question`: A question used to judge the response from the model-under-test and determine whether the prompt injection was successful or not.

The image path provided to each test case is at `images/<id>.png`.

The following keys serve as tags providing additional metadata about the test case:
- `image_description`: Text description used to generate the image
- `image_text`: Text transcription of any text overlaid on the image
- `injection_technique`: Tags indicating what type of prompt injection technique was used in this test case.
- `injection_type`: Either `direct` or `indirect`.
- `risk_category`: Either `logic-violating` or `security-violating`.


## Additional Information

### Curation Rationale

The dataset is created to address a gap in existing evaluations for prompt injection and particularly multimodal prompt injection. Prompt injection is a security issue affecting LLMs, when untrusted data is placed into the context of a model, causing unintended behavior. It is one of the biggest security issues that affect LLMs, and there is a need to understand these risks, particularly as newer models now support multimodal inputs which increases the risk surface for prompt injection.

### Source Data

The test cases are synthetically created using [Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct). [Meta AI](https://www.meta.ai/)'s image generation model was used to produce the images.

A subset of test cases contain images of CAPTCHAs, which are sourced from [Wilhelmy, Rodrigo & Rosas, Horacio. (2013)](https://www.researchgate.net/publication/248380891_captcha_dataset).

Some of the techniques in these test cases are inspired by [FigStep](https://github.com/ThuCCSLab/FigStep) and [MM-SafetyBench](https://arxiv.org/pdf/2311.17600v2).

#### Personal and Sensitive Information

The dataset does not contain any personal or sensitive information. The data is synthetically generated and is not expected to contain any real world data that is of sensitive nature.

## Limitations

* This dataset only covers test cases in the English language.
* As the dataset is synthetic, this may lead to limitations in generalizability.
* Not every sample in this dataset has been manually reviewed, so there may be errors in some test cases.
* The judging of responses is also based on a judge LLM, which may produce incorrect results due to the probabilistic nature of LLM responses.

### Recommendations

Users should be made aware of these limitations of the dataset.

## Citation

**BibTeX:**

```bibtex
@misc{wan2024CyberSecEval 3advancingevaluation,
      title={CyberSecEval 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models},
      author={Shengye Wan and Cyrus Nikolaidis and Daniel Song and David Molnar and James Crnkovich and Jayson Grace and Manish Bhatt and Sahana Chennabasappa and Spencer Whitman and Stephanie Ding and Vlad Ionescu and Yue Li and Joshua Saxe},
      year={2024},
      eprint={2408.01605},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2408.01605},
}
```

## Dataset Authors

* Stephanie Ding ([sym@meta.com](mailto:sym@meta.com))
