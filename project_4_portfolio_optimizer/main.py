from market_data import download_prices
from portfolio import (
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio,
)
from monte_carlo import simulate_portfolios

import matplotlib.pyplot as plt
import numpy as np


#User inputs---------------------------------------------------------------------------------------------------

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
start_date = "2021-01-01"
risk_free_rate = 0.04
number_of_portfolios = 10000
investment_amount = 1000000
investment_duration_years = 5


#Market data---------------------------------------------------------------------------------------------------

prices = download_prices(tickers, start_date)
returns = prices.pct_change().dropna()

annual_returns = returns.mean() * 252
covariance_matrix = returns.cov() * 252

print("\nExpected individual annual returns:")
print(annual_returns.apply(lambda value: f"{value:.2%}"))

print("\nAnnual covariance matrix:")
print(covariance_matrix)


#Equal-weight portfolio scenario-----------------------------------------------------------------------------------------

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


#Monte Carlo simulation--------------------------------------------------------------------------------------

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


# Find the simulated portfolio with the highest Sharpe ratio
maximum_sharpe_index = np.argmax(simulated_sharpes)

maximum_sharpe = simulated_sharpes[maximum_sharpe_index]
maximum_sharpe_return = simulated_returns[maximum_sharpe_index]
maximum_sharpe_volatility = simulated_volatilities[maximum_sharpe_index]
maximum_sharpe_weights = simulated_weights_list[maximum_sharpe_index]


print("\n--- MONTE CARLO MAXIMUM-SHARPE PORTFOLIO ---")
print(f"Expected return: {maximum_sharpe_return:.2%}")
print(f"Volatility: {maximum_sharpe_volatility:.2%}")
print(f"Sharpe ratio: {maximum_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, maximum_sharpe_weights):
    print(f"{ticker}: {weight:.2%}")


# Find the simulated portfolio with the lowest volatility
minimum_volatility_index = np.argmin(simulated_volatilities)

minimum_volatility = simulated_volatilities[minimum_volatility_index]
minimum_volatility_return = simulated_returns[minimum_volatility_index]
minimum_volatility_sharpe = simulated_sharpes[minimum_volatility_index]
minimum_volatility_weights = simulated_weights_list[minimum_volatility_index]


print("\n--- MONTE CARLO MINIMUM-VOLATILITY PORTFOLIO ---")
print(f"Expected return: {minimum_volatility_return:.2%}")
print(f"Volatility: {minimum_volatility:.2%}")
print(f"Sharpe ratio: {minimum_volatility_sharpe:.2f}")

print("\nWeights:")
for ticker, weight in zip(tickers, minimum_volatility_weights):
    print(f"{ticker}: {weight:.2%}")

#Perspective help------------------------------------------------------------------------------------------------

investment_amount = investment_amount * (1 + maximum_sharpe_return) ** investment_timelapse

print(
    f"\nIf you invest ${investment_amount:,.0f} in the maximum Sharpe portfolio, after {investment_timelapse} years you will have ${investment_amount:,.2f}."
)

# Chart----------------------------------------------------------------------------------------------------------

plt.scatter(
    simulated_volatilities,
    simulated_returns,
    c=simulated_sharpes,
    alpha=0.65,
)

plt.scatter(
    maximum_sharpe_volatility,
    maximum_sharpe_return,
    marker="*",
    s=220,
    label="Maximum Sharpe",
)

plt.scatter(
    minimum_volatility,
    minimum_volatility_return,
    marker="*",
    s=220,
    label="Minimum Volatility",
)

plt.title("Monte Carlo Portfolio Simulation")
plt.xlabel("Annual Volatility")
plt.ylabel("Expected Annual Return")
plt.colorbar(label="Sharpe Ratio")
plt.legend()
plt.tight_layout()

# Open the chart in a window
plt.show()
