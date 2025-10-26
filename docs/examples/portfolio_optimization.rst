Portfolio Optimization
======================

This example demonstrates how to use qfinbox for portfolio optimization using modern portfolio theory.

Basic Mean-Variance Optimization
---------------------------------

.. code-block:: python

    import qfinbox as qfb
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Generate sample data (replace with real data)
    np.random.seed(42)
    n_assets = 5
    n_periods = 252

    # Simulate asset returns
    returns = np.random.multivariate_normal(
        mean=[0.08, 0.12, 0.10, 0.15, 0.06],
        cov=np.array([
            [0.16, 0.02, 0.03, 0.01, 0.02],
            [0.02, 0.25, 0.04, 0.02, 0.01],
            [0.03, 0.04, 0.20, 0.03, 0.02],
            [0.01, 0.02, 0.03, 0.30, 0.01],
            [0.02, 0.01, 0.02, 0.01, 0.12]
        ]) / 252,
        size=n_periods
    )

    # Convert to DataFrame
    asset_names = ['Asset A', 'Asset B', 'Asset C', 'Asset D', 'Asset E']
    returns_df = pd.DataFrame(returns, columns=asset_names)

    print("Sample returns data:")
    print(returns_df.head())

Expected Returns and Covariance
-------------------------------

.. code-block:: python

    # Calculate expected returns and covariance matrix
    expected_returns = returns_df.mean() * 252  # Annualized
    cov_matrix = returns_df.cov() * 252  # Annualized

    print("\\nExpected Returns (Annualized):")
    print(expected_returns)

    print("\\nCovariance Matrix (Annualized):")
    print(cov_matrix)

Efficient Frontier
------------------

.. code-block:: python

    # Example efficient frontier calculation (placeholder)
    # This would be implemented in the actual qfinbox library

    def calculate_portfolio_metrics(weights, returns, cov_matrix):
        \"\"\"Calculate portfolio return and volatility.\"\"\"
        portfolio_return = np.sum(returns * weights)
        portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return portfolio_return, portfolio_vol

    # Generate random portfolios for demonstration
    n_portfolios = 10000
    results = np.zeros((3, n_portfolios))

    np.random.seed(42)
    for i in range(n_portfolios):
        # Random weights
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)  # Normalize to sum to 1

        # Calculate metrics
        port_return, port_vol = calculate_portfolio_metrics(
            weights, expected_returns, cov_matrix
        )

        results[0, i] = port_return
        results[1, i] = port_vol
        results[2, i] = port_return / port_vol  # Sharpe ratio approximation

    # Plot efficient frontier
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1], results[0], c=results[2], cmap='viridis', alpha=0.5)
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Expected Return')
    plt.title('Efficient Frontier - Random Portfolios')
    plt.show()

Optimal Portfolio Weights
-------------------------

.. code-block:: python

    # Find portfolio with maximum Sharpe ratio
    max_sharpe_idx = np.argmax(results[2])
    max_sharpe_return = results[0, max_sharpe_idx]
    max_sharpe_vol = results[1, max_sharpe_idx]

    print(f"\\nMaximum Sharpe Ratio Portfolio:")
    print(f"Expected Return: {max_sharpe_return:.4f}")
    print(f"Volatility: {max_sharpe_vol:.4f}")
    print(f"Sharpe Ratio: {results[2, max_sharpe_idx]:.4f}")

Risk Budgeting
--------------

.. code-block:: python

    # Example risk budgeting (equal risk contribution)
    # This would be implemented in the actual qfinbox library

    def equal_risk_contribution_weights(cov_matrix, tolerance=1e-6, max_iter=1000):
        \"\"\"Calculate equal risk contribution portfolio weights.\"\"\"
        n = cov_matrix.shape[0]
        weights = np.ones(n) / n  # Start with equal weights

        for iteration in range(max_iter):
            # Risk contribution calculation
            portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            marginal_contrib = np.dot(cov_matrix, weights) / portfolio_vol
            contrib = weights * marginal_contrib

            # Check convergence
            target_contrib = np.sum(contrib) / n
            if np.max(np.abs(contrib - target_contrib)) < tolerance:
                break

            # Update weights (simplified approach)
            weights = weights * target_contrib / contrib
            weights = weights / np.sum(weights)  # Normalize

        return weights

    # Calculate ERC weights
    erc_weights = equal_risk_contribution_weights(cov_matrix)

    print("\\nEqual Risk Contribution Portfolio:")
    for i, (asset, weight) in enumerate(zip(asset_names, erc_weights)):
        print(f"{asset}: {weight:.4f}")

Advanced Optimization
---------------------

.. code-block:: python

    # Example with constraints (placeholder for actual implementation)
    # In the real qfinbox library, this would use optimization libraries

    from scipy.optimize import minimize

    def portfolio_volatility(weights, cov_matrix):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    def portfolio_return(weights, expected_returns):
        return np.sum(expected_returns * weights)

    # Constraint: weights sum to 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    # Bounds: long-only portfolio (0 <= weight <= 1)
    bounds = tuple((0, 1) for _ in range(n_assets))

    # Minimize volatility for a target return
    target_return = 0.10

    def objective(weights):
        return portfolio_volatility(weights, cov_matrix)

    # Add return constraint
    constraints_with_return = [
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type': 'eq', 'fun': lambda x: portfolio_return(x, expected_returns) - target_return}
    ]

    # Initial guess
    x0 = np.ones(n_assets) / n_assets

    # Optimize
    result = minimize(objective, x0, method='SLSQP',
                     bounds=bounds, constraints=constraints_with_return)

    if result.success:
        optimal_weights = result.x
        print(f"\\nMinimum Variance Portfolio for {target_return:.2%} target return:")
        for asset, weight in zip(asset_names, optimal_weights):
            print(f"{asset}: {weight:.4f}")

        opt_return = portfolio_return(optimal_weights, expected_returns)
        opt_vol = portfolio_volatility(optimal_weights, cov_matrix)
        print(f"\\nPortfolio Return: {opt_return:.4f}")
        print(f"Portfolio Volatility: {opt_vol:.4f}")

Next Steps
----------

This example provides a foundation for portfolio optimization. In practice, you would:

1. Use real market data
2. Consider transaction costs
3. Add additional constraints (sector limits, turnover constraints)
4. Implement robust optimization techniques
5. Perform out-of-sample testing

See the qfinbox API documentation for more advanced optimization methods.
