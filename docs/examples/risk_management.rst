Risk Management
===============

This example demonstrates comprehensive risk management using qfinbox tools.

Value at Risk (VaR)
-------------------

.. code-block:: python

    import qfinbox as qfb
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy import stats

    # Generate sample portfolio returns
    np.random.seed(42)
    n_periods = 1000
    
    # Simulate returns with some volatility clustering
    returns = []
    sigma = 0.02
    for i in range(n_periods):
        if i > 0 and abs(returns[i-1]) > 0.03:
            sigma = 0.03  # Higher volatility after large moves
        else:
            sigma = 0.02  # Normal volatility
        
        returns.append(np.random.normal(0.0005, sigma))
    
    returns = np.array(returns)
    dates = pd.date_range('2020-01-01', periods=n_periods, freq='D')
    returns_series = pd.Series(returns, index=dates)
    
    print("Portfolio returns statistics:")
    print(f"Mean: {returns.mean():.6f}")
    print(f"Std: {returns.std():.6f}")
    print(f"Skewness: {stats.skew(returns):.4f}")
    print(f"Kurtosis: {stats.kurtosis(returns):.4f}")

Historical VaR
--------------

.. code-block:: python

    def historical_var(returns, confidence=0.95):
        \"\"\"Calculate historical Value at Risk.\"\"\"
        return np.percentile(returns, (1 - confidence) * 100)
    
    def historical_cvar(returns, confidence=0.95):
        \"\"\"Calculate historical Conditional Value at Risk (Expected Shortfall).\"\"\"
        var = historical_var(returns, confidence)
        return returns[returns <= var].mean()
    
    # Calculate VaR and CVaR at different confidence levels
    confidence_levels = [0.90, 0.95, 0.99]
    
    print("\\nHistorical VaR and CVaR:")
    for conf in confidence_levels:
        var = historical_var(returns, conf)
        cvar = historical_cvar(returns, conf)
        print(f"{conf:.0%} VaR: {var:.4f} ({var*100:.2f}%)")
        print(f"{conf:.0%} CVaR: {cvar:.4f} ({cvar*100:.2f}%)")
        print()

Parametric VaR
--------------

.. code-block:: python

    def parametric_var(returns, confidence=0.95, distribution='normal'):
        \"\"\"Calculate parametric VaR assuming normal distribution.\"\"\"
        mean = returns.mean()
        std = returns.std()
        
        if distribution == 'normal':
            z_score = stats.norm.ppf(1 - confidence)
            return mean + z_score * std
        elif distribution == 't':
            # Fit t-distribution
            params = stats.t.fit(returns)
            return stats.t.ppf(1 - confidence, *params)
    
    print("Parametric VaR (Normal Distribution):")
    for conf in confidence_levels:
        var_normal = parametric_var(returns, conf, 'normal')
        var_t = parametric_var(returns, conf, 't')
        print(f"{conf:.0%} VaR (Normal): {var_normal:.4f}")
        print(f"{conf:.0%} VaR (t-dist): {var_t:.4f}")
        print()

Monte Carlo VaR
---------------

.. code-block:: python

    def monte_carlo_var(returns, confidence=0.95, n_simulations=10000):
        \"\"\"Calculate Monte Carlo VaR.\"\"\"
        # Fit parameters to historical data
        mean = returns.mean()
        std = returns.std()
        
        # Generate simulated returns
        simulated_returns = np.random.normal(mean, std, n_simulations)
        
        return np.percentile(simulated_returns, (1 - confidence) * 100)
    
    print("Monte Carlo VaR:")
    for conf in confidence_levels:
        mc_var = monte_carlo_var(returns, conf)
        print(f"{conf:.0%} VaR (Monte Carlo): {mc_var:.4f}")

VaR Backtesting
---------------

.. code-block:: python

    def var_backtest(returns, confidence=0.95, window=250):
        \"\"\"Backtest VaR model using rolling window.\"\"\"
        violations = []
        var_estimates = []
        
        for i in range(window, len(returns)):
            # Calculate VaR using rolling window
            window_returns = returns[i-window:i]
            var_estimate = historical_var(window_returns, confidence)
            var_estimates.append(var_estimate)
            
            # Check if actual return violates VaR
            actual_return = returns[i]
            violation = actual_return < var_estimate
            violations.append(violation)
        
        return np.array(violations), np.array(var_estimates)
    
    # Perform backtesting
    violations, var_estimates = var_backtest(returns, 0.95, 250)
    
    violation_rate = violations.mean()
    expected_rate = 0.05  # 5% for 95% confidence
    
    print(f"\\nVaR Backtesting Results (95% confidence):")
    print(f"Violation rate: {violation_rate:.4f} ({violation_rate*100:.2f}%)")
    print(f"Expected rate: {expected_rate:.4f} ({expected_rate*100:.2f}%)")
    print(f"Number of violations: {violations.sum()}")
    print(f"Total observations: {len(violations)}")

Kupiec Test
-----------

.. code-block:: python

    def kupiec_test(violations, confidence=0.95):
        \"\"\"Perform Kupiec test for VaR model validation.\"\"\"
        n = len(violations)
        x = violations.sum()  # Number of violations
        p = 1 - confidence    # Expected violation rate
        
        if x == 0:
            lr_stat = -2 * n * np.log(1 - p)
        elif x == n:
            lr_stat = -2 * n * np.log(p)
        else:
            lr_stat = -2 * (n * np.log(1 - p) + x * np.log(p / (x/n)) + 
                           (n - x) * np.log((1 - p) / (1 - x/n)))
        
        # Critical value for 95% confidence (chi-squared with 1 df)
        critical_value = stats.chi2.ppf(0.95, 1)
        p_value = 1 - stats.chi2.cdf(lr_stat, 1)
        
        return lr_stat, critical_value, p_value
    
    lr_stat, critical_value, p_value = kupiec_test(violations, 0.95)
    
    print(f"\\nKupiec Test Results:")
    print(f"LR statistic: {lr_stat:.4f}")
    print(f"Critical value (5%): {critical_value:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Reject model: {lr_stat > critical_value}")

Risk Decomposition
------------------

.. code-block:: python

    # Example: Component VaR for a portfolio
    def component_var(weights, returns_matrix, confidence=0.95):
        \"\"\"Calculate component VaR for portfolio positions.\"\"\"
        # Portfolio returns
        portfolio_returns = np.dot(returns_matrix, weights)
        portfolio_var = historical_var(portfolio_returns, confidence)
        
        # Calculate marginal VaR (simplified approach)
        marginal_vars = []
        epsilon = 0.001
        
        for i in range(len(weights)):
            # Perturb weight slightly
            perturbed_weights = weights.copy()
            perturbed_weights[i] += epsilon
            perturbed_weights = perturbed_weights / perturbed_weights.sum()  # Renormalize
            
            perturbed_returns = np.dot(returns_matrix, perturbed_weights)
            perturbed_var = historical_var(perturbed_returns, confidence)
            
            marginal_var = (perturbed_var - portfolio_var) / epsilon
            marginal_vars.append(marginal_var)
        
        # Component VaR = Weight × Marginal VaR
        component_vars = np.array(weights) * np.array(marginal_vars)
        
        return portfolio_var, marginal_vars, component_vars
    
    # Example with 3-asset portfolio
    n_assets = 3
    weights = np.array([0.4, 0.35, 0.25])
    
    # Generate correlated asset returns
    np.random.seed(42)
    correlation_matrix = np.array([
        [1.0, 0.3, 0.2],
        [0.3, 1.0, 0.4], 
        [0.2, 0.4, 1.0]
    ])
    
    returns_matrix = np.random.multivariate_normal(
        [0.0005, 0.0003, 0.0008], 
        correlation_matrix * 0.02**2, 
        1000
    )
    
    portfolio_var, marginal_vars, component_vars = component_var(
        weights, returns_matrix, 0.95
    )
    
    print(f"\\nComponent VaR Analysis:")
    print(f"Portfolio 95% VaR: {portfolio_var:.4f}")
    print("\\nAsset Contributions:")
    for i, (w, mvar, cvar) in enumerate(zip(weights, marginal_vars, component_vars)):
        print(f"Asset {i+1}: Weight={w:.3f}, Marginal VaR={mvar:.4f}, Component VaR={cvar:.4f}")

Stress Testing
--------------

.. code-block:: python

    def stress_test_scenarios():
        \"\"\"Define stress test scenarios.\"\"\"
        scenarios = {
            'Market Crash': {'equity': -0.20, 'bonds': -0.05, 'commodities': -0.15},
            'Interest Rate Spike': {'equity': -0.10, 'bonds': -0.15, 'commodities': 0.05},
            'Inflation Surge': {'equity': -0.05, 'bonds': -0.12, 'commodities': 0.20},
            'Credit Crisis': {'equity': -0.25, 'bonds': -0.08, 'commodities': -0.10}
        }
        return scenarios
    
    # Example portfolio allocation
    portfolio = {
        'equity': 0.60,
        'bonds': 0.30, 
        'commodities': 0.10
    }
    
    scenarios = stress_test_scenarios()
    
    print("\\nStress Test Results:")
    for scenario_name, shocks in scenarios.items():
        portfolio_impact = sum(
            portfolio[asset] * shock 
            for asset, shock in shocks.items() 
            if asset in portfolio
        )
        print(f"{scenario_name}: {portfolio_impact:.4f} ({portfolio_impact*100:.2f}%)")

Visualization
-------------

.. code-block:: python

    # Plot VaR evolution
    plt.figure(figsize=(12, 8))
    
    # Plot returns and VaR
    plt.subplot(2, 1, 1)
    test_period = returns[-len(violations):]
    test_dates = dates[-len(violations):]
    
    plt.plot(test_dates, test_period, alpha=0.7, label='Returns')
    plt.plot(test_dates, var_estimates, 'r-', label='95% VaR')
    
    # Highlight violations
    violation_dates = test_dates[violations]
    violation_returns = test_period[violations]
    plt.scatter(violation_dates, violation_returns, color='red', s=20, 
               label=f'Violations ({violations.sum()})')
    
    plt.title('VaR Model Performance')
    plt.ylabel('Returns')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot violation frequency over time
    plt.subplot(2, 1, 2)
    rolling_violations = pd.Series(violations).rolling(window=60).mean()
    plt.plot(test_dates, rolling_violations, label='60-day Rolling Violation Rate')
    plt.axhline(y=0.05, color='r', linestyle='--', label='Expected Rate (5%)')
    plt.ylabel('Violation Rate')
    plt.xlabel('Date')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

Next Steps
----------

This example covers fundamental risk management concepts. Advanced applications include:

1. **Multi-asset portfolio risk**: Correlation modeling and copulas
2. **Dynamic risk models**: GARCH and regime-switching models  
3. **Extreme value theory**: Modeling tail risks
4. **Risk attribution**: Factor-based risk decomposition
5. **Regulatory capital**: Basel III and Solvency II calculations

Explore the qfinbox API for more sophisticated risk management tools.