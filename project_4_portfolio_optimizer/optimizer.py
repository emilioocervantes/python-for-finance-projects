import numpy as np
from scipy.optimize import minimize

from portfolio import (
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio
)


def volatility_objective(weights, covariance_matrix):
    # Return portfolio volatility for SciPy to minimize
    return calculate_portfolio_volatility(
        weights,
        covariance_matrix
    )


def negative_sharpe_objective(
    weights,
    annual_returns,
    covariance_matrix,
    risk_free_rate
):
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

    # Convert maximization into a minimization problem
    return -sharpe_ratio


def optimize_minimum_volatility(
    number_of_assets,
    covariance_matrix
):
    # Start with equal portfolio weights
    initial_weights = (
        np.ones(number_of_assets) / number_of_assets
    )

    # Keep every weight between 0% and 100%
    bounds = tuple(
        (0, 1)
        for _ in range(number_of_assets)
    )

    # Require all weights to sum to 100%
    constraints = {
        "type": "eq",
        "fun": lambda weights: np.sum(weights) - 1
    }

    # Find the portfolio with the lowest volatility
    result = minimize(
        volatility_objective,
        initial_weights,
        args=(covariance_matrix,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return result


def optimize_maximum_sharpe(
    number_of_assets,
    annual_returns,
    covariance_matrix,
    risk_free_rate
):
    # Start with equal portfolio weights
    initial_weights = (
        np.ones(number_of_assets) / number_of_assets
    )

    # Keep every weight between 0% and 100%
    bounds = tuple(
        (0, 1)
        for _ in range(number_of_assets)
    )

    # Require all weights to sum to 100%
    constraints = {
        "type": "eq",
        "fun": lambda weights: np.sum(weights) - 1
    }

    # Find the portfolio with the highest Sharpe ratio
    result = minimize(
        negative_sharpe_objective,
        initial_weights,
        args=(
            annual_returns,
            covariance_matrix,
            risk_free_rate
        ),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return result