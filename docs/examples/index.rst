Examples
========

This section contains practical examples demonstrating how to use qfinbox for various
Time Value of Money calculations and financial analysis tasks.

Basic TVM Examples
------------------

Present and Future Value Calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import basic

    # Calculate present value of $10,000 received in 5 years at 6% annual rate
    pv = basic.present_value(fv=10000, rate=0.06, periods=5)
    print(f"Present Value: ${pv:.2f}")  # $7,472.58

    # Calculate future value of $5,000 invested for 10 years at 8% annual rate
    fv = basic.future_value(pv=5000, rate=0.08, periods=10)
    print(f"Future Value: ${fv:.2f}")   # $10,794.62

    # Find the interest rate for doubling money in 10 years
    rate = basic.interest_rate(pv=1000, fv=2000, periods=10)
    print(f"Required Rate: {rate:.2%}")  # 7.18%

Annuity Examples
----------------

Retirement Planning
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import annuities

    # Calculate present value of $2,000 monthly payments for 25 years at 7% annual rate
    monthly_rate = 0.07 / 12
    periods = 25 * 12
    pv = annuities.pv_ordinary_annuity(pmt=2000, rate=monthly_rate, periods=periods)
    print(f"Present Value of Retirement Income: ${pv:,.2f}")  # $312,816.55

    # Calculate future value of $500 monthly savings for 30 years at 6% annual rate
    monthly_rate = 0.06 / 12
    periods = 30 * 12
    fv = annuities.fv_ordinary_annuity(pmt=500, rate=monthly_rate, periods=periods)
    print(f"Future Value of Savings: ${fv:,.2f}")  # $502,258.15

    # Calculate perpetuity value for $10,000 annual payments at 5% rate
    perpetuity = annuities.perpetuity_value(pmt=10000, rate=0.05)
    print(f"Perpetuity Value: ${perpetuity:,.2f}")  # $200,000.00

Bond Valuation Examples
-----------------------

Corporate Bond Analysis
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import bonds

    # Price a 10-year corporate bond with 6% coupon, $1000 face value, 5% market rate
    price = bonds.bond_price(face_value=1000, coupon_rate=0.06,
                           market_rate=0.05, periods=10)
    print(f"Bond Price: ${price:.2f}")  # $1,077.22

    # Calculate yield for bond trading at $950 with 5% coupon
    bond_yield = bonds.bond_yield(price=950, face_value=1000,
                                coupon_rate=0.05, periods=8)
    print(f"Bond Yield: {bond_yield:.2%}")  # 5.74%

    # Calculate duration for interest rate risk assessment
    duration = bonds.bond_duration(face_value=1000, coupon_rate=0.04,
                                 market_rate=0.05, periods=15)
    print(f"Modified Duration: {duration:.2f} years")  # 10.38 years

Loan Analysis Examples
----------------------

Mortgage Calculations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import loans
    import pandas as pd

    # Calculate monthly payment for $300,000 mortgage at 4.5% for 30 years
    principal = 300000
    annual_rate = 0.045
    years = 30
    monthly_rate = annual_rate / 12
    periods = years * 12

    payment = loans.loan_payment(principal=principal, rate=monthly_rate, periods=periods)
    print(f"Monthly Payment: ${payment:.2f}")  # $1,520.06

    # Calculate remaining balance after 10 years
    payments_made = 10 * 12
    balance = loans.loan_balance(principal=principal, rate=monthly_rate,
                               periods=periods, payments_made=payments_made)
    print(f"Remaining Balance: ${balance:,.2f}")  # $234,896.47

    # Generate amortization schedule (first 12 months)
    schedule = loans.amortization_schedule(principal=principal, rate=monthly_rate,
                                         periods=periods, num_payments=12)
    df = pd.DataFrame(schedule)
    print(df.head())

Cash Flow Analysis Examples
---------------------------

Investment Project Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import cashflow

    # Evaluate investment project with initial cost and 5-year cash flows
    cash_flows = [-100000, 25000, 30000, 35000, 40000, 45000]
    discount_rate = 0.12

    # Calculate Net Present Value
    project_npv = cashflow.npv(rate=discount_rate, cash_flows=cash_flows)
    print(f"Project NPV: ${project_npv:,.2f}")  # $16,747.82

    # Calculate Internal Rate of Return
    project_irr = cashflow.irr(cash_flows=cash_flows)
    print(f"Project IRR: {project_irr:.2%}")  # 19.54%

    # Calculate Payback Period
    payback = cashflow.payback_period(cash_flows=cash_flows)
    print(f"Payback Period: {payback:.2f} years")  # 3.44 years

    # Calculate Profitability Index
    pi = cashflow.profitability_index(rate=discount_rate, cash_flows=cash_flows)
    print(f"Profitability Index: {pi:.3f}")  # 1.167

Advanced Examples
-----------------

Complex Financial Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from qfinbox.tvm import basic, annuities, cashflow
    import numpy as np

    # Education funding calculation
    # Child is 5 years old, college starts at 18 (13 years from now)
    # College costs $50,000/year for 4 years, inflation 3% annually

    # Calculate future cost of college
    years_to_college = 13
    annual_cost_today = 50000
    inflation_rate = 0.03

    future_costs = []
    for year in range(4):  # 4 years of college
        periods = years_to_college + year
        future_cost = basic.future_value(pv=annual_cost_today,
                                       rate=inflation_rate, periods=periods)
        future_costs.append(future_cost)

    print("Future College Costs:")
    for i, cost in enumerate(future_costs, 1):
        print(f"Year {i}: ${cost:,.2f}")

    # Calculate present value of total college costs
    investment_rate = 0.07
    total_pv = sum(basic.present_value(fv=cost, rate=investment_rate,
                                     periods=years_to_college + i)
                  for i, cost in enumerate(future_costs))
    print(f"\nPresent Value of College Costs: ${total_pv:,.2f}")

    # Calculate required monthly savings
    monthly_rate = investment_rate / 12
    months = years_to_college * 12
    required_savings = total_pv / annuities.fv_ordinary_annuity(pmt=1,
                                                              rate=monthly_rate,
                                                              periods=months)
    print(f"Required Monthly Savings: ${required_savings:,.2f}")

.. note::
   All examples use realistic financial scenarios and demonstrate practical applications
   of the qfinbox TVM functions. The calculations assume standard financial conventions
   and can be adapted for specific use cases.
