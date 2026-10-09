import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# Configure the streamlit page
st.set_page_config(layout="wide", page_title="CyberSecEval Leaderboard", page_icon=":bar_chart:")
# Display the title and brief description of the page
st.markdown("# CyberSecEval: Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models (LLMs)", unsafe_allow_html=True)

# Provide more detailed information about the page and its purpose
st.markdown("""
Welcome to the CyberSecEval leaderboard. This platform showcases the results of our cybersecurity evaluation framework applied to various popular LLMs. Our open-source evaluation suite's workings and coverage are detailed in our [first](https://ai.meta.com/research/publications/purple-llama-cyberseceval-a-benchmark-for-evaluating-the-cybersecurity-risks-of-large-language-models/) and [second](https://ai.meta.com/research/publications/cyberseceval-2-a-wide-ranging-cybersecurity-evaluation-suite-for-large-language-models/) papers. 

In the following sections, we present case study test results and provide concise explanations of their implications.

**Take Action:** Measure your own LLM using CyberSecEval! Visit our open-source GitHub repository [here](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks)!
""")

# Load JSON files containing test results
data_attack = json.load(open("attack_helpfulness.json"))
data_interpreter = json.load(open("interpreter_abuse_tests.json"))
data_prompt = json.load(open("prompt_injection_tests.json"))
data_exploit = json.load(open("exploit_tests.json"))
data_tradeoff = json.load(open("trr_frr_tradeoff_helpfulness.json"))

# Function to sort rows and columns by their sums
def sort_df(df):
    return df.loc[df.sum(axis=1).sort_values(ascending=False).index, df.sum(axis=0).sort_values(ascending=False).index]

# Convert JSON data to pandas DataFrames and sort
attack_df = sort_df(pd.DataFrame(data_attack))
interpreter_df = sort_df(pd.DataFrame(data_interpreter))
prompt_df = sort_df(pd.DataFrame(data_prompt))
exploit_df = sort_df(pd.DataFrame(data_exploit))

# Scatterplot for True refusal vs. false refusal results
tradeoff_df = pd.DataFrame(data_tradeoff).transpose()

# Briefly explain the purpose of the scatterplot
st.markdown("### Evaluating LLMs' Assistance to Cyberattackers")
st.markdown("""
We measure the tradeoff between LLMs' 'false refusals' (refusing to assist in legitimate cybersecurity-related activities) and their 'violation rate' (agreeing to assist in offensive cyber attacks). The results are displayed in the scatterplot below.
""")

# Create a new figure
fig = go.Figure()

# Loop through each row and plot with different marker and color
for i, row in enumerate(tradeoff_df.iterrows()):
    fig.add_trace(go.Scatter(x=[row[1]['Violation Rate']], y=[row[1]['Refusal Rate']], 
                             mode='markers', 
                             name=row[0], marker=dict(size=15)))

# Add labels and title
fig.update_layout(title='True Refusal vs. Violation Rate for Cybersecurity Prompts',
                  xaxis_title='Violation Rate',
                  yaxis_title='Refusal Rate',
                  plot_bgcolor='rgba(0,0,0,0)',
                  xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False))

# Describe the plot
st.markdown("""
The plot below evaluates the performance of various LLMs in two tasks:
* Complying with legitimate requests for help with cybersecurity-related tasks
* Refusing to assist in offensive cyberattacks
An ideal LLM would be positioned in the lower left corner of the plot.
""")

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Function to display heatmaps and bar charts
def display_results(df, title, description,include_barchart=True):
    if title:
        st.markdown(f"### {title}")
    st.markdown(f"{description}")
    st.dataframe(df.style.format("{:.2%}").background_gradient(cmap='coolwarm'))
    if include_barchart:
        if title:
            st.markdown(f"### Overall Performance of Models in {title}")
        fig = px.bar(df.sum(axis=1).sort_values(ascending=False))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
              xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig, use_container_width=True)

# Display the results for each test
# Continue displaying the results for each test
display_results(interpreter_df, 'LLMs Assistance to Hack Code Interpreter Environments', 'The plot below shows how often each model complies with attempts to hack a connected code interpreter. Lower values indicate safer models.', False)
display_results(prompt_df, 'LLMs Susceptibility to Prompt Injection Attacks', 'The plot below shows how often each model succumbs to prompt injection attacks, categorized into threat categories detailed in our paper. Lower values indicate safer models.', False)
display_results(exploit_df, 'LLMs Capability to Solve Cyber Capture the Flag Challenges', 'The plot below shows how well each model performs at solving capture-the-flag style program exploitation challenges. Higher values indicate more capable models.', False)

# Load additional JSON files
data_mitre = json.load(open("mitre.json"))
data_insecure = json.load(open("insecure_code.json"))

# Process data for the table
model_stats_insecure = {}
for model, categories in data_insecure.items():
    model_stats_insecure[model] = {'Mean Insecure Code Test Pass Rate': pd.Series([1-v['autocomplete_vunerable_percentage'] for v in categories.values()]).mean()}
    for category, values in categories.items():
        model_stats_insecure[model][f'Insecure Code Test Pass Rate in {category}'] = 1-values['autocomplete_vunerable_percentage']
leaderboard_df_insecure = pd.DataFrame.from_dict(model_stats_insecure, orient='index').sort_values(by='Mean Insecure Code Test Pass Rate', ascending=False)

# Prepare data for the clustered bar chart
chart_data_insecure = []
for model, categories in data_insecure.items():
    for category, values in categories.items():
        chart_data_insecure.append({
            'Model': model,
            'Category': category,
            'Insecure Code Test Pass Rate': 1-values['autocomplete_vunerable_percentage']
        })
chart_df_insecure = pd.DataFrame(chart_data_insecure)

# Style the data table
st.markdown("### LLMs Adherence to Secure Coding Practices in Risky Software Engineering Settings")
st.markdown("""
The table below shows the propensity of LLMs to avoid insecure coding practices when used as coding assistants or software engineering agents. Higher values indicate safer models.
""")
st.dataframe(leaderboard_df_insecure.style.format("{:.2%}").background_gradient(cmap='Blues'))  # Changed cmap to 'Blues'

# Create a Plotly chart
fig_insecure = px.bar(chart_df_insecure, x='Category', y='Insecure Code Test Pass Rate', barmode='group', color='Model',
             title='Category-wise Insecure Code Test Pass Rate per Model',
             labels={'Insecure Code Test Pass Rate': 'Insecure Code Test Pass Rate %'},
             color_discrete_sequence=px.colors.qualitative.Pastel)
fig_insecure.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                  xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False, tickformat=".0%"),
                  legend=dict(title='Models'))

# Display the chart
st.plotly_chart(fig_insecure, use_container_width=True)
