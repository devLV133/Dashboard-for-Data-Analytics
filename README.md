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
