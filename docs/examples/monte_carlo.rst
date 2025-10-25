Backtesting
===========

This example demonstrates strategy backtesting using qfinbox tools.

.. code-block:: python

    import qfinbox as qfb
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta

Simple Moving Average Strategy
------------------------------

.. code-block:: python

    # Generate sample price data
    np.random.seed(42)
    n_days = 1000
    dates = pd.date_range('2021-01-01', periods=n_days, freq='D')

    # Simulate price with trend and noise
    initial_price = 100
    trend = 0.0002  # Small daily trend
    volatility = 0.02

    returns = np.random.normal(trend, volatility, n_days)
    prices = initial_price * np.exp(np.cumsum(returns))

    # Create DataFrame
    data = pd.DataFrame({
        'price': prices,
        'returns': returns
    }, index=dates)

    print("Sample price data:")
    print(data.head())

Monte Carlo Simulation
======================

This example demonstrates Monte Carlo simulation for option pricing and risk assessment.

.. code-block:: python

    import qfinbox as qfb
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

Black-Scholes Monte Carlo
--------------------------

.. code-block:: python

    def black_scholes_monte_carlo(S0, K, T, r, sigma, n_simulations=100000):
        \"\"\"
        Price European options using Monte Carlo simulation.

        Parameters:
        S0: Initial stock price
        K: Strike price
        T: Time to expiration (years)
        r: Risk-free rate
        sigma: Volatility
        n_simulations: Number of Monte Carlo paths
        \"\"\"
        # Generate random paths
        np.random.seed(42)
        Z = np.random.standard_normal(n_simulations)

        # Calculate terminal stock prices
        ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

        # Calculate option payoffs
        call_payoffs = np.maximum(ST - K, 0)
        put_payoffs = np.maximum(K - ST, 0)

        # Discount to present value
        call_price = np.exp(-r * T) * np.mean(call_payoffs)
        put_price = np.exp(-r * T) * np.mean(put_payoffs)

        return call_price, put_price, ST

    # Option parameters
    S0 = 100    # Current stock price
    K = 105     # Strike price
    T = 0.25    # 3 months to expiration
    r = 0.05    # 5% risk-free rate
    sigma = 0.2 # 20% volatility

    call_price, put_price, terminal_prices = black_scholes_monte_carlo(
        S0, K, T, r, sigma, 100000
    )

    print(f"Monte Carlo Option Prices:")
    print(f"Call Price: ${call_price:.4f}")
    print(f"Put Price: ${put_price:.4f}")

Analytical Black-Scholes Comparison
-----------------------------------

.. code-block:: python

    def black_scholes_analytical(S0, K, T, r, sigma):
        \"\"\"Analytical Black-Scholes option pricing.\"\"\"
        d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)

        call_price = S0*stats.norm.cdf(d1) - K*np.exp(-r*T)*stats.norm.cdf(d2)
        put_price = K*np.exp(-r*T)*stats.norm.cdf(-d2) - S0*stats.norm.cdf(-d1)

        return call_price, put_price

    # Compare with analytical solution
    analytical_call, analytical_put = black_scholes_analytical(S0, K, T, r, sigma)

    print(f"\\nAnalytical Black-Scholes Prices:")
    print(f"Call Price: ${analytical_call:.4f}")
    print(f"Put Price: ${analytical_put:.4f}")

    print(f"\\nDifference (Monte Carlo - Analytical):")
    print(f"Call: ${call_price - analytical_call:.4f}")
    print(f"Put: ${put_price - analytical_put:.4f}")

Path-Dependent Options
----------------------

.. code-block:: python

    def asian_option_monte_carlo(S0, K, T, r, sigma, n_steps=50, n_simulations=100000):
        \"\"\"Price Asian (average price) options using Monte Carlo.\"\"\"
        dt = T / n_steps

        # Generate paths
        np.random.seed(42)
        paths = np.zeros((n_simulations, n_steps + 1))
        paths[:, 0] = S0

        for i in range(1, n_steps + 1):
            Z = np.random.standard_normal(n_simulations)
            paths[:, i] = paths[:, i-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
            )

        # Calculate average prices for each path
        average_prices = np.mean(paths[:, 1:], axis=1)

        # Calculate payoffs
        call_payoffs = np.maximum(average_prices - K, 0)
        put_payoffs = np.maximum(K - average_prices, 0)

        # Discount to present value
        asian_call_price = np.exp(-r * T) * np.mean(call_payoffs)
        asian_put_price = np.exp(-r * T) * np.mean(put_payoffs)

        return asian_call_price, asian_put_price, paths, average_prices

    # Price Asian options
    asian_call, asian_put, sample_paths, avg_prices = asian_option_monte_carlo(
        S0, K, T, r, sigma, n_steps=50, n_simulations=10000
    )

    print(f"\\nAsian Option Prices:")
    print(f"Asian Call: ${asian_call:.4f}")
    print(f"Asian Put: ${asian_put:.4f}")

Barrier Options
---------------

.. code-block:: python

    def barrier_option_monte_carlo(S0, K, T, r, sigma, barrier, barrier_type='up-and-out',
                                  n_steps=100, n_simulations=100000):
        \"\"\"Price barrier options using Monte Carlo.\"\"\"
        dt = T / n_steps

        # Generate paths
        np.random.seed(42)
        paths = np.zeros((n_simulations, n_steps + 1))
        paths[:, 0] = S0

        for i in range(1, n_steps + 1):
            Z = np.random.standard_normal(n_simulations)
            paths[:, i] = paths[:, i-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
            )

        # Check barrier conditions
        if barrier_type == 'up-and-out':
            # Option knocked out if price goes above barrier
            knocked_out = np.any(paths > barrier, axis=1)
        elif barrier_type == 'down-and-out':
            # Option knocked out if price goes below barrier
            knocked_out = np.any(paths < barrier, axis=1)
        elif barrier_type == 'up-and-in':
            # Option only active if price goes above barrier
            knocked_out = ~np.any(paths > barrier, axis=1)
        elif barrier_type == 'down-and-in':
            # Option only active if price goes below barrier
            knocked_out = ~np.any(paths < barrier, axis=1)

        # Calculate terminal payoffs (only for non-knocked-out paths)
        terminal_prices = paths[:, -1]
        call_payoffs = np.maximum(terminal_prices - K, 0)
        call_payoffs[knocked_out] = 0  # Set to 0 if knocked out

        # Discount to present value
        barrier_call_price = np.exp(-r * T) * np.mean(call_payoffs)
        knockouts = np.sum(knocked_out)

        return barrier_call_price, knockouts, paths

    # Price barrier options
    barrier_level = 120  # Barrier at $120
    barrier_call, knockouts, barrier_paths = barrier_option_monte_carlo(
        S0, K, T, r, sigma, barrier_level, 'up-and-out', n_simulations=10000
    )

    print(f"\\nBarrier Option Results (Up-and-Out, Barrier=${barrier_level}):")
    print(f"Barrier Call Price: ${barrier_call:.4f}")
    print(f"Paths knocked out: {knockouts}/10000 ({knockouts/100:.1f}%)")
    print(f"Regular European Call: ${call_price:.4f}")

Risk Scenario Generation
------------------------

.. code-block:: python

    def generate_market_scenarios(n_scenarios=1000, time_horizon=252):
        \"\"\"Generate correlated market scenarios for risk assessment.\"\"\"
        np.random.seed(42)

        # Asset parameters (annual)
        assets = ['Stocks', 'Bonds', 'Commodities', 'FX']
        means = np.array([0.08, 0.03, 0.05, 0.0])  # Expected returns

        # Correlation matrix
        correlation = np.array([
            [1.0,  -0.2,  0.3,  0.1],  # Stocks
            [-0.2,  1.0, -0.1,  0.0],  # Bonds
            [0.3,  -0.1,  1.0,  0.2],  # Commodities
            [0.1,   0.0,  0.2,  1.0]   # FX
        ])

        # Volatilities (annual)
        volatilities = np.array([0.16, 0.06, 0.22, 0.12])

        # Convert to covariance matrix
        cov_matrix = np.outer(volatilities, volatilities) * correlation

        # Generate scenarios (daily returns)
        daily_means = means / 252
        daily_cov = cov_matrix / 252

        scenarios = np.random.multivariate_normal(
            daily_means, daily_cov, (n_scenarios, time_horizon)
        )

        # Convert to cumulative returns
        cumulative_returns = np.cumprod(1 + scenarios, axis=1) - 1

        return scenarios, cumulative_returns, assets

    # Generate scenarios
    daily_scenarios, cumulative_scenarios, asset_names = generate_market_scenarios(
        n_scenarios=1000, time_horizon=252
    )

    print(f"\\nGenerated {daily_scenarios.shape[0]} market scenarios")
    print(f"Time horizon: {daily_scenarios.shape[1]} days")
    print(f"Assets: {asset_names}")

Portfolio Risk Assessment
-------------------------

.. code-block:: python

    def portfolio_scenario_analysis(scenarios, weights):
        \"\"\"Analyze portfolio risk using market scenarios.\"\"\"
        # Calculate portfolio returns for each scenario
        portfolio_scenarios = np.dot(scenarios, weights)

        # Calculate risk metrics
        var_95 = np.percentile(portfolio_scenarios[:, -1], 5)
        var_99 = np.percentile(portfolio_scenarios[:, -1], 1)
        cvar_95 = portfolio_scenarios[:, -1][portfolio_scenarios[:, -1] <= var_95].mean()

        # Maximum drawdown for each scenario
        cumulative_portfolio = np.cumprod(1 + portfolio_scenarios, axis=1)
        running_max = np.maximum.accumulate(cumulative_portfolio, axis=1)
        drawdowns = (cumulative_portfolio - running_max) / running_max
        max_drawdowns = np.min(drawdowns, axis=1)

        results = {
            'scenarios': portfolio_scenarios,
            'var_95': var_95,
            'var_99': var_99,
            'cvar_95': cvar_95,
            'max_drawdown_95': np.percentile(max_drawdowns, 95),
            'max_drawdown_worst': np.min(max_drawdowns)
        }

        return results

    # Example portfolio weights
    portfolio_weights = np.array([0.6, 0.2, 0.15, 0.05])  # 60% stocks, 20% bonds, etc.

    # Analyze portfolio risk
    risk_results = portfolio_scenario_analysis(daily_scenarios, portfolio_weights)

    print(f"\\nPortfolio Risk Analysis (1-year horizon):")
    print(f"95% VaR: {risk_results['var_95']:.4f} ({risk_results['var_95']*100:.2f}%)")
    print(f"99% VaR: {risk_results['var_99']:.4f} ({risk_results['var_99']*100:.2f}%)")
    print(f"95% CVaR: {risk_results['cvar_95']:.4f} ({risk_results['cvar_95']*100:.2f}%)")
    print(f"95% Max Drawdown: {risk_results['max_drawdown_95']:.4f} ({risk_results['max_drawdown_95']*100:.2f}%)")
    print(f"Worst Case Drawdown: {risk_results['max_drawdown_worst']:.4f} ({risk_results['max_drawdown_worst']*100:.2f}%)")

Visualization
-------------

.. code-block:: python

    # Create comprehensive visualization
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    # 1. Sample price paths for option pricing
    axes[0, 0].plot(sample_paths[:20].T, alpha=0.7)
    axes[0, 0].axhline(y=K, color='r', linestyle='--', label=f'Strike ${K}')
    axes[0, 0].set_title('Sample Price Paths\\n(First 20 simulations)')
    axes[0, 0].set_xlabel('Time Steps')
    axes[0, 0].set_ylabel('Stock Price')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 2. Terminal price distribution
    axes[0, 1].hist(terminal_prices, bins=50, alpha=0.7, density=True)
    axes[0, 1].axvline(K, color='r', linestyle='--', label=f'Strike ${K}')
    axes[0, 1].set_title('Terminal Price Distribution')
    axes[0, 1].set_xlabel('Terminal Stock Price')
    axes[0, 1].set_ylabel('Density')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # 3. Barrier option paths
    axes[0, 2].plot(barrier_paths[:10].T, alpha=0.7)
    axes[0, 2].axhline(y=barrier_level, color='r', linestyle='-',
                      linewidth=2, label=f'Barrier ${barrier_level}')
    axes[0, 2].axhline(y=K, color='g', linestyle='--', label=f'Strike ${K}')
    axes[0, 2].set_title('Barrier Option Paths\\n(First 10 simulations)')
    axes[0, 2].set_xlabel('Time Steps')
    axes[0, 2].set_ylabel('Stock Price')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)

    # 4. Portfolio scenario returns
    portfolio_final_returns = risk_results['scenarios'][:, -1]
    axes[1, 0].hist(portfolio_final_returns, bins=50, alpha=0.7)
    axes[1, 0].axvline(risk_results['var_95'], color='r', linestyle='--',
                      label=f"95% VaR: {risk_results['var_95']:.3f}")
    axes[1, 0].axvline(risk_results['var_99'], color='darkred', linestyle='--',
                      label=f"99% VaR: {risk_results['var_99']:.3f}")
    axes[1, 0].set_title('Portfolio Return Distribution\\n(1-year horizon)')
    axes[1, 0].set_xlabel('Portfolio Return')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # 5. Correlation matrix heatmap
    import seaborn as sns
    correlation_data = np.corrcoef(daily_scenarios[:, -1, :].T)
    im = axes[1, 1].imshow(correlation_data, cmap='RdBu', vmin=-1, vmax=1)
    axes[1, 1].set_xticks(range(len(asset_names)))
    axes[1, 1].set_yticks(range(len(asset_names)))
    axes[1, 1].set_xticklabels(asset_names, rotation=45)
    axes[1, 1].set_yticklabels(asset_names)
    axes[1, 1].set_title('Asset Correlation Matrix')

    # Add correlation values as text
    for i in range(len(asset_names)):
        for j in range(len(asset_names)):
            text = axes[1, 1].text(j, i, f'{correlation_data[i, j]:.2f}',
                                  ha="center", va="center", color="black")

    # 6. Sample portfolio paths
    sample_portfolio_paths = np.cumprod(1 + risk_results['scenarios'][:50], axis=1)
    axes[1, 2].plot(sample_portfolio_paths.T, alpha=0.5)
    axes[1, 2].set_title('Sample Portfolio Paths\\n(First 50 scenarios)')
    axes[1, 2].set_xlabel('Days')
    axes[1, 2].set_ylabel('Portfolio Value (Normalized)')
    axes[1, 2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

Advanced Applications
---------------------

This example demonstrates the foundation for Monte Carlo methods in finance.
Advanced applications include:

1. **Exotic Options**: Lookback, rainbow, and basket options
2. **Credit Risk**: Default probability modeling and CVA calculations
3. **Market Risk**: Stress testing and scenario generation
4. **Operational Risk**: Loss distribution modeling
5. **Model Risk**: Parameter uncertainty and model validation

The Monte Carlo framework in qfinbox provides the flexibility to implement
these advanced applications efficiently.
