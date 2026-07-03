import numpy as np


def calculate_portfolio_return(weights, annual_returns):
    # Calculate the portfolio's expected annual return
    portfolio_return = np.dot(weights, annual_returns)

    return portfolio_return


def calculate_portfolio_volatility(weights, covariance_matrix):
    # Calculate portfolio variance using asset weights and covariances
    portfolio_variance = np.dot(
        weights.T,
        np.dot(covariance_matrix, weights)
    )

    # Convert variance into annual volatility
    portfolio_volatility = np.sqrt(portfolio_variance)

    return portfolio_volatility


def calculate_sharpe_ratio(
    portfolio_return,
    portfolio_volatility,
    risk_free_rate
):
    # Measure excess return earned per unit of risk
    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return sharpe_ratio