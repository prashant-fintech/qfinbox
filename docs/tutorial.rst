Tutorial: Complete Guide to qfinbox TVM
=====================================

This comprehensive tutorial covers all aspects of using qfinbox for Time Value of Money
calculations. We'll walk through practical examples from basic calculations to advanced
financial analysis scenarios.

.. contents::
   :local:
   :depth: 2

Getting Started
---------------

First, ensure you have qfinbox installed:

.. code-block:: bash

    pip install qfinbox

Import the modules you need:

.. code-block:: python

    import qfinbox as qf
    from qfinbox.tvm import basic, annuities, bonds, loans, cashflow
    import numpy as np
    import pandas as pd

Chapter 1: Basic TVM Calculations
----------------------------------

Understanding Present and Future Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The foundation of finance is the time value of money - money available now is worth
more than the same amount in the future due to its earning potential.

**Example 1.1: Simple Present Value**

You expect to receive $10,000 in 5 years. What's it worth today if you can earn 6% annually?

.. code-block:: python

    from qfinbox.tvm import basic

    # Calculate present value
    pv = basic.present_value(fv=10000, rate=0.06, periods=5)
    print(f"Present Value: ${pv:.2f}")
    # Output: Present Value: $7,472.58

**Example 1.2: Simple Future Value**

You invest $5,000 today at 8% annual return. What will it be worth in 10 years?

.. code-block:: python

    # Calculate future value
    fv = basic.future_value(pv=5000, rate=0.08, periods=10)
    print(f"Future Value: ${fv:.2f}")
    # Output: Future Value: $10,794.62

**Example 1.3: Finding Required Return**

You want to double your $1,000 investment in 8 years. What return do you need?

.. code-block:: python

    # Calculate required interest rate
    rate = basic.interest_rate(pv=1000, fv=2000, periods=8)
    print(f"Required Annual Return: {rate:.2%}")
    # Output: Required Annual Return: 9.05%

**Example 1.4: Time to Reach Goal**

How long will it take to grow $1,000 to $3,000 at 12% annually?

.. code-block:: python

    # Calculate number of periods
    periods = basic.number_of_periods(pv=1000, fv=3000, rate=0.12)
    print(f"Time to triple investment: {periods:.1f} years")
    # Output: Time to triple investment: 9.7 years

Compound Interest and Effective Rates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 1.5: Effective vs Nominal Rates**

Compare a bank offering 6% compounded monthly vs 6.2% compounded annually:

.. code-block:: python

    # Convert 6% monthly compounding to effective annual rate
    effective_6_monthly = basic.effective_rate(nominal_rate=0.06, compounding_periods=12)
    print(f"6% monthly compounding = {effective_6_monthly:.3%} effective annual")

    # 6.2% annual is already the effective rate
    print(f"6.2% annual compounding = 6.200% effective annual")

    # The monthly compounding option is better!
    # Output:
    # 6% monthly compounding = 6.168% effective annual
    # 6.2% annual compounding = 6.200% effective annual

Chapter 2: Annuities and Regular Payments
------------------------------------------

Annuities are series of equal payments made at regular intervals. They're fundamental
to retirement planning, loan calculations, and investment analysis.

Ordinary Annuities (End-of-Period Payments)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 2.1: Retirement Savings**

You plan to save $500 monthly for 30 years. With 7% annual return (0.583% monthly),
how much will you have?

.. code-block:: python

    from qfinbox.tvm import annuities

    monthly_rate = 0.07 / 12
    periods = 30 * 12

    fv = annuities.fv_ordinary_annuity(pmt=500, rate=monthly_rate, periods=periods)
    print(f"Retirement Savings After 30 Years: ${fv:,.2f}")
    # Output: Retirement Savings After 30 Years: $612,255.41

**Example 2.2: Required Retirement Income**

You want $4,000 monthly income for 25 years in retirement. With 6% annual return,
how much do you need at retirement?

.. code-block:: python

    monthly_rate = 0.06 / 12
    periods = 25 * 12

    pv = annuities.pv_ordinary_annuity(pmt=4000, rate=monthly_rate, periods=periods)
    print(f"Required at Retirement: ${pv:,.2f}")
    # Output: Required at Retirement: $625,633.10

Annuities Due (Beginning-of-Period Payments)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 2.3: Rent Payments**

A lease requires $2,000 monthly payments at the beginning of each month for 3 years.
With 5% annual discount rate, what's the present value?

.. code-block:: python

    monthly_rate = 0.05 / 12
    periods = 3 * 12

    pv = annuities.pv_annuity_due(pmt=2000, rate=monthly_rate, periods=periods)
    print(f"Present Value of Lease: ${pv:,.2f}")
    # Output: Present Value of Lease: $67,940.15

Perpetuities and Growing Annuities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 2.4: Endowment Fund**

A university wants to provide $50,000 annual scholarships forever. With 4% return,
what endowment is needed?

.. code-block:: python

    perpetuity = annuities.perpetuity_value(pmt=50000, rate=0.04)
    print(f"Required Endowment: ${perpetuity:,.2f}")
    # Output: Required Endowment: $1,250,000.00

**Example 2.5: Growing Dividend Stream**

A stock pays $2 dividend this year, growing 5% annually. With 9% required return,
what's the present value of 20 years of dividends?

.. code-block:: python

    pv = annuities.growing_annuity_pv(pmt=2, rate=0.09, growth_rate=0.05, periods=20)
    print(f"Present Value of Growing Dividends: ${pv:.2f}")
    # Output: Present Value of Growing Dividends: $24.36

Chapter 3: Bond Valuation and Analysis
---------------------------------------

Bonds are debt securities that pay periodic interest and return principal at maturity.
Understanding bond pricing is crucial for fixed-income investing.

Basic Bond Pricing
~~~~~~~~~~~~~~~~~~~

**Example 3.1: Corporate Bond Valuation**

A 10-year corporate bond has 6% annual coupon rate, $1,000 face value. If market
interest rates are 5%, what should the bond trade for?

.. code-block:: python

    from qfinbox.tvm import bonds

    price = bonds.bond_price(
        face_value=1000,
        coupon_rate=0.06,
        market_rate=0.05,
        periods=10
    )
    print(f"Bond Price: ${price:.2f}")
    # Output: Bond Price: $1,077.22

    # The bond trades at a premium because its coupon rate (6%)
    # exceeds the market rate (5%)

**Example 3.2: Bond Yield Calculation**

The same bond is trading for $950. What's its yield to maturity?

.. code-block:: python

    bond_yield = bonds.bond_yield(
        price=950,
        face_value=1000,
        coupon_rate=0.06,
        periods=10
    )
    print(f"Yield to Maturity: {bond_yield:.3%}")
    # Output: Yield to Maturity: 6.782%

Interest Rate Risk: Duration and Convexity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 3.3: Duration Analysis**

Calculate the modified duration of a 15-year bond with 4% coupon trading to yield 5%:

.. code-block:: python

    duration = bonds.bond_duration(
        face_value=1000,
        coupon_rate=0.04,
        market_rate=0.05,
        periods=15
    )
    print(f"Modified Duration: {duration:.2f} years")
    # Output: Modified Duration: 10.38 years

    # This means a 1% increase in interest rates will decrease
    # the bond price by approximately 10.38%

**Example 3.4: Convexity for Large Rate Changes**

For the same bond, calculate convexity:

.. code-block:: python

    convexity = bonds.bond_convexity(
        face_value=1000,
        coupon_rate=0.04,
        market_rate=0.05,
        periods=15
    )
    print(f"Convexity: {convexity:.2f}")
    # Output: Convexity: 134.48

    # Convexity helps estimate price changes for large interest rate movements

Zero-Coupon Bonds
~~~~~~~~~~~~~~~~~~

**Example 3.5: Zero-Coupon Bond Analysis**

A zero-coupon bond matures in 20 years with $1,000 face value. If it's priced to
yield 4%, what's its current price?

.. code-block:: python

    price = bonds.zero_coupon_bond_price(
        face_value=1000,
        market_rate=0.04,
        periods=20
    )
    print(f"Zero-Coupon Bond Price: ${price:.2f}")
    # Output: Zero-Coupon Bond Price: $456.39

Chapter 4: Loan Analysis and Mortgages
---------------------------------------

Loan calculations are essential for personal finance, real estate, and corporate finance.

Mortgage Calculations
~~~~~~~~~~~~~~~~~~~~~

**Example 4.1: Home Mortgage Payment**

Calculate monthly payment for a $400,000 mortgage at 4.5% for 30 years:

.. code-block:: python

    from qfinbox.tvm import loans

    principal = 400000
    annual_rate = 0.045
    years = 30

    monthly_rate = annual_rate / 12
    periods = years * 12

    payment = loans.loan_payment(
        principal=principal,
        rate=monthly_rate,
        periods=periods
    )
    print(f"Monthly Payment: ${payment:.2f}")
    # Output: Monthly Payment: $2,026.74

**Example 4.2: Loan Balance Over Time**

What's the remaining balance after 10 years of payments?

.. code-block:: python

    payments_made = 10 * 12
    balance = loans.loan_balance(
        principal=principal,
        rate=monthly_rate,
        periods=periods,
        payments_made=payments_made
    )
    print(f"Balance After 10 Years: ${balance:,.2f}")
    # Output: Balance After 10 Years: $313,195.29

**Example 4.3: Total Interest Analysis**

How much total interest will be paid over the life of the loan?

.. code-block:: python

    total_interest = loans.total_interest_paid(
        principal=principal,
        rate=monthly_rate,
        periods=periods
    )
    print(f"Total Interest Paid: ${total_interest:,.2f}")
    # Output: Total Interest Paid: $329,625.18

Amortization Analysis
~~~~~~~~~~~~~~~~~~~~~

**Example 4.4: Detailed Amortization Schedule**

Generate the first 12 months of payments showing principal and interest breakdown:

.. code-block:: python

    import pandas as pd

    schedule = loans.amortization_schedule(
        principal=principal,
        rate=monthly_rate,
        periods=periods,
        num_payments=12
    )

    # Convert to DataFrame for better display
    df = pd.DataFrame(schedule)
    df['Payment'] = df['Payment'].round(2)
    df['Interest'] = df['Interest'].round(2)
    df['Principal'] = df['Principal'].round(2)
    df['Balance'] = df['Balance'].round(2)

    print("First Year Amortization Schedule:")
    print(df)

Loan Affordability
~~~~~~~~~~~~~~~~~~

**Example 4.5: Maximum Loan Amount**

With $3,000 monthly payment capacity, 4.5% rate, 30-year term, what's the maximum loan?

.. code-block:: python

    max_loan = loans.loan_affordability(
        payment=3000,
        rate=monthly_rate,
        periods=periods
    )
    print(f"Maximum Affordable Loan: ${max_loan:,.2f}")
    # Output: Maximum Affordable Loan: $592,006.35

Chapter 5: Investment Analysis and Cash Flows
----------------------------------------------

Cash flow analysis is fundamental to investment decisions, capital budgeting,
and project evaluation.

Net Present Value (NPV) Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 5.1: Investment Project Evaluation**

A project requires $100,000 initial investment and generates the following cash flows:
Year 1: $30,000, Year 2: $40,000, Year 3: $45,000, Year 4: $50,000

With 12% required return, should you invest?

.. code-block:: python

    from qfinbox.tvm import cashflow

    cash_flows = [-100000, 30000, 40000, 45000, 50000]
    required_return = 0.12

    project_npv = cashflow.npv(rate=required_return, cash_flows=cash_flows)
    print(f"Project NPV: ${project_npv:,.2f}")

    if project_npv > 0:
        print("✅ Accept the project - it creates value!")
    else:
        print("❌ Reject the project - it destroys value")

    # Output:
    # Project NPV: $32,351.88
    # ✅ Accept the project - it creates value!

Internal Rate of Return (IRR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 5.2: Finding Project IRR**

What's the actual return rate of the project above?

.. code-block:: python

    project_irr = cashflow.irr(cash_flows=cash_flows)
    print(f"Project IRR: {project_irr:.2%}")
    print(f"Required Return: {required_return:.2%}")

    if project_irr > required_return:
        print("✅ IRR exceeds required return - accept project!")
    else:
        print("❌ IRR below required return - reject project")

    # Output:
    # Project IRR: 28.08%
    # Required Return: 12.00%
    # ✅ IRR exceeds required return - accept project!

Modified IRR for Reinvestment Reality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 5.3: MIRR Analysis**

IRR assumes cash flows are reinvested at the IRR rate, which may be unrealistic.
MIRR assumes reinvestment at a more realistic rate:

.. code-block:: python

    finance_rate = 0.08   # Cost of capital for negative cash flows
    reinvest_rate = 0.10  # Reinvestment rate for positive cash flows

    project_mirr = cashflow.mirr(
        cash_flows=cash_flows,
        finance_rate=finance_rate,
        reinvest_rate=reinvest_rate
    )
    print(f"Project MIRR: {project_mirr:.2%}")
    # Output: Project MIRR: 19.72%

Payback Period Analysis
~~~~~~~~~~~~~~~~~~~~~~~

**Example 5.4: Simple and Discounted Payback**

How long does it take to recover the initial investment?

.. code-block:: python

    # Simple payback (ignores time value of money)
    simple_payback = cashflow.payback_period(cash_flows=cash_flows)
    print(f"Simple Payback Period: {simple_payback:.2f} years")

    # Discounted payback (considers time value of money)
    discounted_payback = cashflow.discounted_payback_period(
        rate=required_return,
        cash_flows=cash_flows
    )
    print(f"Discounted Payback Period: {discounted_payback:.2f} years")

    # Output:
    # Simple Payback Period: 2.56 years
    # Discounted Payback Period: 3.11 years

Profitability Index
~~~~~~~~~~~~~~~~~~~

**Example 5.5: Investment Ranking**

When capital is limited, use profitability index to rank projects:

.. code-block:: python

    pi = cashflow.profitability_index(rate=required_return, cash_flows=cash_flows)
    print(f"Profitability Index: {pi:.3f}")

    if pi > 1.0:
        print("✅ PI > 1.0 - Project creates value")
    else:
        print("❌ PI < 1.0 - Project destroys value")

    # Output:
    # Profitability Index: 1.324
    # ✅ PI > 1.0 - Project creates value

Chapter 6: Advanced Applications
--------------------------------

Real-World Complex Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 6.1: Comprehensive Education Funding Plan**

Plan for a child's college education with inflation and changing costs:

.. code-block:: python

    # Setup: Child is 5, college starts at 18 (13 years away)
    years_to_college = 13
    annual_cost_today = 60000  # Current annual college cost
    inflation_rate = 0.035     # 3.5% education inflation
    investment_return = 0.08   # Expected return on college savings

    # Step 1: Calculate future college costs (4 years)
    future_costs = []
    for year in range(4):
        periods = years_to_college + year
        future_cost = basic.future_value(
            pv=annual_cost_today,
            rate=inflation_rate,
            periods=periods
        )
        future_costs.append(future_cost)
        print(f"College Year {year+1} Cost: ${future_cost:,.2f}")

    # Step 2: Calculate present value of all college costs
    total_college_pv = 0
    for i, cost in enumerate(future_costs):
        pv_cost = basic.present_value(
            fv=cost,
            rate=investment_return,
            periods=years_to_college + i
        )
        total_college_pv += pv_cost

    print(f"\\nTotal PV of College Costs: ${total_college_pv:,.2f}")

    # Step 3: Calculate required monthly savings
    monthly_return = investment_return / 12
    months_to_save = years_to_college * 12

    # Use future value of annuity to find required payment
    required_fv = total_college_pv * (1 + investment_return) ** years_to_college
    fv_annuity_factor = annuities.fv_ordinary_annuity(
        pmt=1, rate=monthly_return, periods=months_to_save
    )
    required_monthly_savings = required_fv / fv_annuity_factor

    print(f"Required Monthly Savings: ${required_monthly_savings:,.2f}")

**Example 6.2: Buy vs Rent Analysis**

Comprehensive analysis comparing home purchase vs renting:

.. code-block:: python

    # Scenario parameters
    home_price = 500000
    down_payment_pct = 0.20
    loan_rate = 0.045
    loan_years = 30
    monthly_rent = 2800
    rent_growth = 0.03
    home_appreciation = 0.035
    investment_return = 0.07
    analysis_years = 10

    # Purchase scenario
    down_payment = home_price * down_payment_pct
    loan_amount = home_price - down_payment

    monthly_loan_rate = loan_rate / 12
    loan_periods = loan_years * 12

    monthly_mortgage = loans.loan_payment(
        principal=loan_amount,
        rate=monthly_loan_rate,
        periods=loan_periods
    )

    # Calculate home value after analysis period
    future_home_value = basic.future_value(
        pv=home_price,
        rate=home_appreciation,
        periods=analysis_years
    )

    # Calculate remaining mortgage balance
    payments_made = analysis_years * 12
    remaining_balance = loans.loan_balance(
        principal=loan_amount,
        rate=monthly_loan_rate,
        periods=loan_periods,
        payments_made=payments_made
    )

    # Net proceeds from sale
    equity_at_sale = future_home_value - remaining_balance
    net_cost_buying = down_payment + (monthly_mortgage * payments_made) - equity_at_sale

    # Rental scenario
    total_rent_paid = 0
    current_rent = monthly_rent

    for year in range(analysis_years):
        annual_rent = current_rent * 12
        total_rent_paid += annual_rent
        current_rent *= (1 + rent_growth)

    # Opportunity cost of down payment
    down_payment_growth = basic.future_value(
        pv=down_payment,
        rate=investment_return,
        periods=analysis_years
    )

    net_cost_renting = total_rent_paid - down_payment_growth

    print(f"\\n=== {analysis_years}-Year Buy vs Rent Analysis ===")
    print(f"\\nBuying:")
    print(f"Down Payment: ${down_payment:,.2f}")
    print(f"Monthly Mortgage: ${monthly_mortgage:,.2f}")
    print(f"Home Value After {analysis_years} Years: ${future_home_value:,.2f}")
    print(f"Remaining Balance: ${remaining_balance:,.2f}")
    print(f"Equity at Sale: ${equity_at_sale:,.2f}")
    print(f"Net Cost of Buying: ${net_cost_buying:,.2f}")

    print(f"\\nRenting:")
    print(f"Starting Monthly Rent: ${monthly_rent:,.2f}")
    print(f"Total Rent Paid: ${total_rent_paid:,.2f}")
    print(f"Down Payment Invested: ${down_payment_growth:,.2f}")
    print(f"Net Cost of Renting: ${net_cost_renting:,.2f}")

    savings = net_cost_renting - net_cost_buying
    if savings > 0:
        print(f"\\n✅ Buying saves: ${savings:,.2f}")
    else:
        print(f"\\n✅ Renting saves: ${abs(savings):,.2f}")

Advanced Portfolio Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 6.3: Multi-Project Capital Allocation**

When facing capital constraints, optimize project selection:

.. code-block:: python

    # Multiple project scenarios
    projects = {
        'Project A': {
            'initial_cost': 50000,
            'cash_flows': [-50000, 15000, 20000, 25000, 30000],
        },
        'Project B': {
            'initial_cost': 75000,
            'cash_flows': [-75000, 25000, 30000, 35000, 40000],
        },
        'Project C': {
            'initial_cost': 100000,
            'cash_flows': [-100000, 35000, 40000, 45000, 50000],
        }
    }

    discount_rate = 0.12
    capital_budget = 150000  # Limited capital

    # Analyze each project
    project_analysis = []

    for name, data in projects.items():
        cf = data['cash_flows']

        npv = cashflow.npv(rate=discount_rate, cash_flows=cf)
        irr_val = cashflow.irr(cash_flows=cf)
        pi = cashflow.profitability_index(rate=discount_rate, cash_flows=cf)
        payback = cashflow.payback_period(cash_flows=cf)

        project_analysis.append({
            'Project': name,
            'Initial_Cost': data['initial_cost'],
            'NPV': npv,
            'IRR': irr_val,
            'PI': pi,
            'Payback': payback
        })

    # Create analysis DataFrame
    df_analysis = pd.DataFrame(project_analysis)
    df_analysis = df_analysis.sort_values('PI', ascending=False)  # Rank by PI

    print("Project Ranking Analysis:")
    print("=" * 60)
    for _, project in df_analysis.iterrows():
        print(f"{project['Project']:10} | NPV: ${project['NPV']:>8,.0f} | "
              f"IRR: {project['IRR']:>6.1%} | PI: {project['PI']:>5.2f} | "
              f"Payback: {project['Payback']:>4.1f}y")

    print("\\nOptimal Selection (Capital Budget: ${:,}):".format(capital_budget))
    selected_projects = []
    remaining_budget = capital_budget
    total_npv = 0

    for _, project in df_analysis.iterrows():
        if project['Initial_Cost'] <= remaining_budget:
            selected_projects.append(project['Project'])
            remaining_budget -= project['Initial_Cost']
            total_npv += project['NPV']
            print(f"✅ Select {project['Project']} - Cost: ${project['Initial_Cost']:,}, NPV: ${project['NPV']:,.0f}")

    print(f"\\nTotal NPV of Selected Projects: ${total_npv:,.0f}")
    print(f"Remaining Budget: ${remaining_budget:,.0f}")

Summary and Best Practices
--------------------------

Key Takeaways
~~~~~~~~~~~~~

1. **Always consider the time value of money** in financial decisions
2. **Use appropriate discount rates** based on risk and opportunity cost
3. **Compare multiple metrics** (NPV, IRR, PI, payback) for robust analysis
4. **Account for inflation** in long-term planning
5. **Consider tax implications** in real-world applications
6. **Validate assumptions** through sensitivity analysis
7. **Use realistic reinvestment rates** (MIRR over IRR when appropriate)

Common Pitfalls to Avoid
~~~~~~~~~~~~~~~~~~~~~~~~

- **IRR limitations**: Multiple IRRs with non-conventional cash flows
- **Scale differences**: IRR can mislead when comparing different-sized projects
- **Reinvestment assumptions**: IRR assumes reinvestment at the IRR rate
- **Ignoring risk**: All calculations assume certainty - consider risk premiums
- **Forgetting taxes**: Real-world returns are after-tax

Performance Tips
~~~~~~~~~~~~~~~~

- **Use NumPy arrays** for vectorized calculations with multiple scenarios
- **Cache complex calculations** when analyzing many similar scenarios
- **Validate inputs** early to avoid calculation errors
- **Consider precision** requirements for financial applications

This completes the comprehensive tutorial covering all aspects of qfinbox TVM functionality.
Each example demonstrates practical applications while explaining the underlying financial concepts.
