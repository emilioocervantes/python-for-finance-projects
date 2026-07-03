import numpy as np

from portfolio import (
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio
)


def simulate_portfolios(
    number_of_portfolios,
    number_of_assets,
    annual_returns,
    covariance_matrix,
    risk_free_rate
):
    # Store the results of every simulated portfolio
    simulated_returns = []
    simulated_volatilities = []
    simulated_sharpes = []
    simulated_weights_list = []

    for _ in range(number_of_portfolios):
        # Generate random portfolio weights that sum to 100%
        weights = np.random.random(number_of_assets)
        weights = weights / weights.sum()

        # Calculate portfolio performance
        portfolio_return = calculate_portfolio_return(
            weights,
            annual_returns
        )

        portfolio_volatility = calculate_portfolio_volatility(
            weights,
            covariance_matrix
        )

        sharpe_ratio = calculate_sharpe_ratio(
            portfolio_return,
            portfolio_volatility,
            risk_free_rate
        )

        # Save the results
        simulated_returns.append(portfolio_return)
        simulated_volatilities.append(portfolio_volatility)
        simulated_sharpes.append(sharpe_ratio)
        simulated_weights_list.append(weights)

    # Return all simulated portfolio data
    return (
        simulated_returns,
        simulated_volatilities,
        simulated_sharpes,
        simulated_weights_list
    )