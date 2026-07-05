# Monte Carlo Portfolio Simulator

A Python project that uses historical market data and Monte Carlo simulation to analyze different portfolio allocations.

The program:

* Downloads historical stock prices with `yfinance`
* Calculates annualized returns and covariance
* Measures portfolio return, volatility, and Sharpe ratio
* Simulates thousands of random portfolios
* Identifies the portfolio with the highest Sharpe ratio
* Identifies the portfolio with the lowest volatility
* Generates a risk-return chart

## Project Structure

```text
main.py
market_data.py
portfolio.py
monte_carlo.py
requirements.txt
README.md
```

## Installation

```bash
git clone https://github.com/emilioocervantes/python-for-finance-projects.git
cd python-for-finance-projects/project_4_portfolio_optimizer
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The program will print the portfolio results and generate:

```text
monte_carlo_simulation.png
```

## Requirements

```text
yfinance
pandas
numpy
matplotlib
```

## Disclaimer

This project uses historical data and is intended for educational purposes only. It should not be considered investment advice.
