# Banking Analytics Dashboard

A runnable Jupyter/Google Colab dashboard for exploring public daily prices for Barclays, HSBC, Lloyds, NatWest and Standard Chartered.

## What it does

- Retrieves split/dividend-adjusted closing prices through yfinance.
- Removes missing, non-numeric, non-finite and non-positive prices and duplicate dates.
- Shows period return, annualised daily-return volatility and actual observation dates.
- Provides interactive line/area charts and a moving-average control.
- Optionally asks OpenAI to explain the currently loaded price summary.

## Run

1. Open [FTSE100_Banking_Analysis_Public_Pilot.ipynb](FTSE100_Banking_Analysis_Public_Pilot.ipynb) in Google Colab or Jupyter.
2. Run Sections 1–3 in order. The setup cell installs yfinance, pandas, numpy, plotly, ipywidgets and openai.
3. Select a bank and period, then click **Load prices**. Market-data retrieval needs internet access.
4. Change the chart type or moving-average window to redraw the loaded data. Changing bank or period clears the old view; click **Load prices** again.
5. For optional AI explanations, set `OPENAI_API_KEY` in the runtime and run Section 4, then click **Explain view**. Do not save a key in the notebook. `OPENAI_MODEL` overrides the default `gpt-4.1-mini`.

The dashboard works without an API key. AI requests require access to the selected model and may incur charges. No GPU is needed.

## Calculations and scope

Period return is `(last adjusted close / first adjusted close - 1) × 100`. Annualised volatility is the sample standard deviation of daily percentage returns multiplied by `sqrt(252)`. Dividends are already reflected in adjusted closes and are not added again. Quote units come from Yahoo Finance and are not necessarily pounds.

This is a public pilot, not the full dissertation research system. It does not retrieve news, validate current FTSE membership, run an agent workflow or independently verify AI explanations. It shows one selected bank at a time.

## Checks

After installing the notebook dependencies, run `python -m unittest discover -s tests -v`. The tests use the notebook's actual functions and cover invalid prices, insufficient observations, duplicate dates, returns and sample volatility without external API calls.

## Troubleshooting

- Missing imports or widgets: run the setup and following cells in order, then restart the kernel if the installation requests it.
- No usable data: check the connection, select another period or retry later. The provider may return incomplete data or limit requests.
- AI unavailable: check the runtime key, model access and account balance. The price dashboard remains usable.

Clear outputs before publishing a run containing private questions or session information.
