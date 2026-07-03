from market_data import download_prices
from portfolio import (
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio,
)
from monte_carlo import simulate_portfolios
from optimizer import (
    optimize_minimum_volatility,
    optimize_maximum_sharpe,
)

import matplotlib.pyplot as plt
import numpy as np


# -------------------- Configuration --------------------

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
start_date = "2021-01-01"
risk_free_rate = 0.04
number_of_portfolios = 10000


# -------------------- Market data --------------------

prices = download_prices(tickers, start_date)
returns = prices.pct_change().dropna()

annual_returns = returns.mean() * 252
covariance_matrix = returns.cov() * 252

print("\nExpected annual returns:")
print(annual_returns.apply(lambda x: f"{x:.2%}"))

print("\nAnnual covariance matrix:")
print(covariance_matrix)


# -------------------- Equal-weight portfolio --------------------

equal_weights = np.ones(len(tickers)) / len(tickers)

equal_return = calculate_portfolio_return(
    equal_weights,
    annual_returns,
)

equal_volatility = calculate_portfolio_volatility(
    equal_weights,
    covariance_matrix,
)

equal_sharpe = calculate_sharpe_ratio(
    equal_return,
    equal_volatility,
    risk_free_rate,
)

print("\n--- EQUAL-WEIGHT PORTFOLIO ---")
print(f"Expected return: {equal_return:.2%}")
print(f"Volatility: {equal_volatility:.2%}")
print(f"Sharpe ratio: {equal_sharpe:.2f}")


# -------------------- SciPy optimization --------------------

minimum_volatility_result = optimize_minimum_volatility(
    len(tickers),
    covariance_matrix,
)

maximum_sharpe_result = optimize_maximum_sharpe(
    len(tickers),
    annual_returns,
    covariance_matrix,
    risk_free_rate,
)

if not minimum_volatility_result.success:
    print("Minimum-volatility optimization failed.")
    print(minimum_volatility_result.message)

if not maximum_sharpe_result.success:
    print("Maximum-Sharpe optimization failed.")
    print(maximum_sharpe_result.message)

# Exact minimum-volatility portfolio

scipy_minimum_weights = minimum_volatility_result.x

scipy_minimum_return = calculate_portfolio_return(
    scipy_minimum_weights,
    annual_returns,
)

scipy_minimum_volatility = calculate_portfolio_volatility(
    scipy_minimum_weights,
    covariance_matrix,
)

scipy_minimum_sharpe = calculate_sharpe_ratio(
    scipy_minimum_return,
    scipy_minimum_volatility,
    risk_free_rate,
)

print("\n--- SCIPY MINIMUM-VOLATILITY PORTFOLIO ---")
print(f"Expected return: {scipy_minimum_return:.2%}")
print(f"Volatility: {scipy_minimum_volatility:.2%}")
print(f"Sharpe ratio: {scipy_minimum_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, scipy_minimum_weights):
    print(f"{ticker}: {weight:.2%}")


# Exact maximum-Sharpe portfolio

scipy_maximum_weights = maximum_sharpe_result.x

scipy_maximum_return = calculate_portfolio_return(
    scipy_maximum_weights,
    annual_returns,
)

scipy_maximum_volatility = calculate_portfolio_volatility(
    scipy_maximum_weights,
    covariance_matrix,
)

scipy_maximum_sharpe = calculate_sharpe_ratio(
    scipy_maximum_return,
    scipy_maximum_volatility,
    risk_free_rate,
)

print("\n--- SCIPY MAXIMUM-SHARPE PORTFOLIO ---")
print(f"Expected return: {scipy_maximum_return:.2%}")
print(f"Volatility: {scipy_maximum_volatility:.2%}")
print(f"Sharpe ratio: {scipy_maximum_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, scipy_maximum_weights):
    print(f"{ticker}: {weight:.2%}")


# -------------------- Monte Carlo simulation --------------------

(
    simulated_returns,
    simulated_volatilities,
    simulated_sharpes,
    simulated_weights_list,
) = simulate_portfolios(
    number_of_portfolios,
    len(tickers),
    annual_returns,
    covariance_matrix,
    risk_free_rate,
)

best_sharpe_index = np.argmax(simulated_sharpes)

monte_carlo_maximum_sharpe = simulated_sharpes[best_sharpe_index]
monte_carlo_maximum_return = simulated_returns[best_sharpe_index]
monte_carlo_maximum_volatility = simulated_volatilities[best_sharpe_index]
monte_carlo_maximum_weights = simulated_weights_list[best_sharpe_index]

minimum_volatility_index = np.argmin(simulated_volatilities)

monte_carlo_minimum_volatility = simulated_volatilities[
    minimum_volatility_index
]
monte_carlo_minimum_return = simulated_returns[
    minimum_volatility_index
]
monte_carlo_minimum_sharpe = simulated_sharpes[
    minimum_volatility_index
]
monte_carlo_minimum_weights = simulated_weights_list[
    minimum_volatility_index
]


print("\n--- MONTE CARLO MAXIMUM-SHARPE PORTFOLIO ---")
print(f"Expected return: {monte_carlo_maximum_return:.2%}")
print(f"Volatility: {monte_carlo_maximum_volatility:.2%}")
print(f"Sharpe ratio: {monte_carlo_maximum_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, monte_carlo_maximum_weights):
    print(f"{ticker}: {weight:.2%}")


print("\n--- MONTE CARLO MINIMUM-VOLATILITY PORTFOLIO ---")
print(f"Expected return: {monte_carlo_minimum_return:.2%}")
print(f"Volatility: {monte_carlo_minimum_volatility:.2%}")
print(f"Sharpe ratio: {monte_carlo_minimum_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, monte_carlo_minimum_weights):
    print(f"{ticker}: {weight:.2%}")


# -------------------- Comparison --------------------

print("\n--- MONTE CARLO VS SCIPY ---")

print("\nMaximum Sharpe ratio:")
print(f"Monte Carlo: {monte_carlo_maximum_sharpe:.4f}")
print(f"SciPy:       {scipy_maximum_sharpe:.4f}")

print("\nMinimum volatility:")
print(f"Monte Carlo: {monte_carlo_minimum_volatility:.4%}")
print(f"SciPy:       {scipy_minimum_volatility:.4%}")


# -------------------- Chart --------------------

plt.scatter(
    simulated_volatilities,
    simulated_returns,
    c=simulated_sharpes,
    alpha=0.65,
)

plt.scatter(
    monte_carlo_maximum_volatility,
    monte_carlo_maximum_return,
    marker="*",
    s=220,
    label="Monte Carlo Maximum Sharpe",
)

plt.scatter(
    monte_carlo_minimum_volatility,
    monte_carlo_minimum_return,
    marker="*",
    s=220,
    label="Monte Carlo Minimum Volatility",
)

plt.scatter(
    scipy_maximum_volatility,
    scipy_maximum_return,
    marker="X",
    s=140,
    label="SciPy Maximum Sharpe",
)

plt.scatter(
    scipy_minimum_volatility,
    scipy_minimum_return,
    marker="X",
    s=140,
    label="SciPy Minimum Volatility",
)

plt.title("Monte Carlo Portfolio Simulation")
plt.xlabel("Annual Volatility")
plt.ylabel("Expected Annual Return")
plt.colorbar(label="Sharpe Ratio")
plt.legend()

plt.savefig(
    "monte_carlo_simulation.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close()

print("\nChart saved as monte_carlo_simulation.png")
