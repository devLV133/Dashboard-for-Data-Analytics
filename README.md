# FTSE 100 Banking Analysis — Public Pilot

A small, runnable demonstration of a banking analytics dashboard based on public price data. This is not the full research application.

## What it shows

- Select a UK-listed bank and a lookback period.
- View adjusted daily prices, returns and an interactive Plotly chart.
- Optionally request a short OpenAI explanation based on the selected market-data summary.

## Run

1. Open `FTSE100_Banking_Analysis_Public_Pilot.ipynb` in Google Colab or Jupyter.
2. Run the setup and dashboard cells in order, then click **Load prices**.
3. For the optional AI button, run Section 4 and set `OPENAI_API_KEY` in the runtime (do not save it in the file). You may override `OPENAI_MODEL`.

Live public prices require internet. The optional AI function requires OpenAI API access and may incur charges. It is not a full retrieval or validation pipeline; do not treat its output as independently verified.

## REQUIREMENTS

- Internet access.
- Google Colab or a local Jupyter environment with Python.
- An OpenAI API key and access to your chosen model for AI chat.
- No GPU is needed.

The first cell installs pandas, matplotlib, yfinance, openai and Gradio. You can leave the API key blank to use only the comparison table and chart.

HOW TO RUN

1. Open the notebook.
Download AI_Banking_Research_Mini.ipynb. Upload it at https://colab.research.google.com/ or open it in Jupyter.

2. Install dependencies.
Run the first code cell and wait for installation to finish. If prompted to restart the session, do so before continuing.

3. Configure the pilot.
Run the configuration cell. The defaults are Barclays and HSBC over three months. Change SELECTED_BANKS and PERIOD if needed. Supported periods are 1mo, 3mo, 6mo and 1y.

Set MODEL to a model available through your OpenAI API account. The notebook defaults to gpt-6-luna; this setting does not verify availability. Enter your API key at the hidden prompt, or press Enter for data-only use.

4. Prepare market-data functions.
Run the Public market data cell. This defines the retrieval and comparison functions. No visible output is expected yet.

5. Generate the comparison.
Run the Example comparison cell. It retrieves prices and displays a return table and chart. The table shows the actual shared comparison dates. Returns use split/dividend-adjusted closes; dividends are not added again.

6. Prepare AI responses.
Run the Basic AI response cell. This defines the chat function without sending an AI request.

7. Launch the chat interface.
Run the Chat interface cell. In Colab, choose a password when prompted. Open the displayed interface or generated link. Sign in with username researcher and the password you chose. Local Jupyter normally displays the interface without this Colab login step.

8. Ask a question.
Select banks and a period in the interface. Try: Compare these banks and show the actual dates.

Change the dropdowns for a different comparison and clear the chat after changing scope. The pilot does not automatically change the controls based on your question. Keep the notebook session running while chatting. Each submitted AI question uses your OpenAI API account.

TROUBLESHOOTING

Missing package or undefined function: Run the preceding cells in order.
No usable price data: Retry later or select different banks.
AI request fails: Check your API key, model access and connection.
Embedded chat does not open: Open the generated Gradio link in a separate tab.

SCOPE AND VALIDATION

This pilot supports price comparisons. News retrieval, advanced analysis and the full research workflow are not included. Core logic passed offline checks; live API and browser execution were not tested here.

Clear outputs before publishing a run containing private questions or session links. Do not put your API key directly into notebook code.
