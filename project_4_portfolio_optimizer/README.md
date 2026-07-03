# Portfolio Optimizer

A Python-based portfolio optimization project that uses historical market data, Monte Carlo simulation, and mathematical optimization to compare portfolio allocations based on expected return, volatility, and Sharpe ratio.

## Overview

This project downloads historical stock prices, calculates portfolio risk and return metrics, simulates random portfolio allocations, and identifies:

* The maximum-Sharpe portfolio
* The minimum-volatility portfolio

The project uses two different approaches:

1. **Monte Carlo simulation**, which evaluates randomly generated portfolios.
2. **SciPy optimization**, which searches mathematically for the optimal portfolio weights.

The results from both approaches are then compared.

## Features

* Downloads historical stock data using `yfinance`
* Calculates daily returns
* Calculates annualized expected returns
* Calculates the annualized covariance matrix
* Evaluates an equal-weight portfolio
* Calculates portfolio expected return
* Calculates portfolio volatility
* Calculates the Sharpe ratio
* Generates random portfolio weights
* Simulates multiple portfolios using Monte Carlo
* Identifies the simulated maximum-Sharpe portfolio
* Identifies the simulated minimum-volatility portfolio
* Calculates exact optimized portfolios using SciPy
* Compares Monte Carlo results against SciPy optimization
* Saves a risk-return visualization as a PNG file

## Default Portfolio

The default portfolio contains:

* Apple (`AAPL`)
* Microsoft (`MSFT`)
* NVIDIA (`NVDA`)
* Amazon (`AMZN`)
* Alphabet (`GOOGL`)

The default historical analysis begins on:

```text
2021-01-01
```

The project uses an assumed annual risk-free rate of:

```text
4%
```

These settings can be changed at the top of `main.py`.

## Project Structure

```text
project_4_portfolio_optimizer/
├── main.py
├── market_data.py
├── portfolio.py
├── monte_carlo.py
├── optimizer.py
├── requirements.txt
├── README.md
└── monte_carlo_simulation.png
```

### File Responsibilities

#### `main.py`

Coordinates the entire project:

* Downloads market data
* Calculates returns and covariance
* Evaluates portfolios
* Runs Monte Carlo simulation
* Runs SciPy optimization
* Prints the results
* Generates the chart

#### `market_data.py`

Downloads and cleans historical closing-price data using `yfinance`.

#### `portfolio.py`

Contains the portfolio calculation functions:

* Expected return
* Volatility
* Sharpe ratio

#### `monte_carlo.py`

Generates random portfolio allocations and calculates the metrics for every simulated portfolio.

#### `optimizer.py`

Uses `scipy.optimize.minimize` to calculate:

* The exact minimum-volatility portfolio
* The exact maximum-Sharpe portfolio

## Installation

Clone the full repository:

```bash
git clone https://github.com/emilioocervantes/python-for-finance-projects.git
```

Enter the project directory:

```bash
cd python-for-finance-projects/project_4_portfolio_optimizer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses:

```text
yfinance
pandas
numpy
matplotlib
scipy
```

## Usage

Run the project with:

```bash
python main.py
```

The script will:

1. Download historical prices.
2. Calculate daily returns.
3. Calculate expected annual returns.
4. Calculate the annual covariance matrix.
5. Evaluate an equal-weight portfolio.
6. Run the SciPy optimizations.
7. Run the Monte Carlo simulation.
8. Compare both approaches.
9. Save the resulting chart.

The generated chart will be saved as:

```text
monte_carlo_simulation.png
```

## Portfolio Metrics

### Expected Return

The expected portfolio return is calculated as the weighted average of the expected returns of the individual assets.

```text
Portfolio Return = Weights · Expected Returns
```

### Portfolio Volatility

Portfolio volatility accounts for:

* The volatility of each asset
* The allocation assigned to each asset
* The covariance between the assets

```text
Portfolio Volatility =
√(Weightsᵀ × Covariance Matrix × Weights)
```

### Sharpe Ratio

The Sharpe ratio measures expected excess return relative to portfolio volatility.

```text
Sharpe Ratio =
(Portfolio Return − Risk-Free Rate) / Portfolio Volatility
```

A higher Sharpe ratio indicates a higher historical return per unit of risk under the assumptions used by the model.

## Monte Carlo Simulation

The Monte Carlo simulation creates multiple random portfolio allocations.

For each portfolio:

1. Random weights are generated.
2. The weights are normalized to sum to 100%.
3. Expected return is calculated.
4. Volatility is calculated.
5. Sharpe ratio is calculated.
6. The resulting metrics and weights are stored.

The simulation then identifies:

* The portfolio with the highest Sharpe ratio
* The portfolio with the lowest volatility

Monte Carlo does not guarantee the exact mathematical optimum because it only evaluates the randomly generated allocations.

## SciPy Optimization

SciPy searches directly for portfolio weights that optimize a specific objective.

### Minimum-Volatility Portfolio

The optimizer minimizes portfolio volatility.

### Maximum-Sharpe Portfolio

Because SciPy minimizes objective functions, the project minimizes the negative Sharpe ratio.

```text
Minimize: −Sharpe Ratio
```

This is mathematically equivalent to maximizing the Sharpe ratio.

## Optimization Constraints

The SciPy optimizations use the following constraints:

* Every portfolio weight must be between 0% and 100%.
* All portfolio weights must sum to 100%.
* Short selling is not permitted.
* The entire portfolio is allocated across the selected assets.

## Monte Carlo vs. SciPy

The project compares:

```text
Maximum Sharpe:
Monte Carlo result vs. SciPy result
```

```text
Minimum Volatility:
Monte Carlo result vs. SciPy result
```

SciPy should generally produce:

* A Sharpe ratio equal to or higher than the Monte Carlo maximum
* A volatility equal to or lower than the Monte Carlo minimum

This happens because SciPy performs direct mathematical optimization, while Monte Carlo evaluates only a finite sample of random portfolios.

## Visualization

The chart plots:

* **X-axis:** annual portfolio volatility
* **Y-axis:** expected annual return
* **Point values:** simulated portfolios
* **Point color:** Sharpe ratio

The chart also highlights:

* Monte Carlo maximum-Sharpe portfolio
* Monte Carlo minimum-volatility portfolio
* SciPy maximum-Sharpe portfolio
* SciPy minimum-volatility portfolio

## Limitations

This model relies on historical market data and simplifying assumptions.

Its results are sensitive to:

* The selected assets
* The historical period
* The estimated expected returns
* Historical volatility
* Historical correlations
* The assumed risk-free rate
* The number of Monte Carlo simulations
* The restriction against short selling

Historical performance does not guarantee future results.

The optimized allocations may also be highly concentrated in assets that performed strongly during the selected historical period.

## Disclaimer

This project was created for educational and analytical purposes.

It does not constitute investment advice, financial advice, or a recommendation to buy or sell any security.

## Author

**Emilio Ortiz Cervantes**

Finance student building projects involving:

* Financial analysis
* Portfolio analytics
* Market data
* Python
* Quantitative finance concepts
