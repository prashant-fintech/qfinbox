Time Value of Money (TVM) Module
==================================

The ``qfinbox.tvm`` module provides comprehensive Time Value of Money calculations
across five specialized submodules. Each module contains functions optimized for
specific types of financial calculations.

.. currentmodule:: qfinbox.tvm

Submodules Overview
-------------------

.. autosummary::
   :toctree: generated/

   basic
   annuities
   bonds
   loans
   cashflow

Basic TVM Calculations (``qfinbox.tvm.basic``)
-----------------------------------------------

Fundamental time value of money calculations for present value, future value,
interest rates, and time periods.

.. automodule:: qfinbox.tvm.basic
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions:

* ``present_value()`` - Calculate present value given future value, rate, and periods
* ``future_value()`` - Calculate future value given present value, rate, and periods
* ``interest_rate()`` - Calculate interest rate given present/future values and periods
* ``number_of_periods()`` - Calculate number of periods given present/future values and rate
* ``effective_rate()`` - Convert nominal rate to effective annual rate
* ``nominal_rate()`` - Convert effective rate to nominal rate with compounding

Annuities (``qfinbox.tvm.annuities``)
--------------------------------------

Calculations for ordinary annuities, annuities due, perpetuities, and growing annuities.

.. automodule:: qfinbox.tvm.annuities
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions:

* ``pv_ordinary_annuity()`` - Present value of ordinary annuity
* ``fv_ordinary_annuity()`` - Future value of ordinary annuity
* ``pv_annuity_due()`` - Present value of annuity due
* ``fv_annuity_due()`` - Future value of annuity due
* ``perpetuity_value()`` - Value of perpetual annuity
* ``growing_annuity_pv()`` - Present value of growing annuity
* ``growing_perpetuity_value()`` - Value of growing perpetuity

Bond Valuation (``qfinbox.tvm.bonds``)
---------------------------------------

Comprehensive bond pricing, yield calculations, and risk measures.

.. automodule:: qfinbox.tvm.bonds
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions:

* ``bond_price()`` - Calculate bond price given coupon rate and market yield
* ``bond_yield()`` - Calculate yield to maturity given bond price
* ``bond_duration()`` - Calculate modified duration for interest rate sensitivity
* ``bond_convexity()`` - Calculate convexity for advanced interest rate risk
* ``zero_coupon_bond_price()`` - Price zero-coupon bonds
* ``zero_coupon_bond_yield()`` - Calculate yield for zero-coupon bonds

Loan Analysis (``qfinbox.tvm.loans``)
--------------------------------------

Comprehensive loan calculations including payments, balances, and amortization schedules.

.. automodule:: qfinbox.tvm.loans
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions:

* ``loan_payment()`` - Calculate periodic loan payment
* ``loan_balance()`` - Calculate remaining loan balance
* ``amortization_schedule()`` - Generate detailed amortization schedule
* ``total_interest_paid()`` - Calculate total interest over loan life
* ``loan_affordability()`` - Determine maximum affordable loan amount

Cash Flow Analysis (``qfinbox.tvm.cashflow``)
----------------------------------------------

Investment analysis tools including NPV, IRR, payback period, and profitability metrics.

.. automodule:: qfinbox.tvm.cashflow
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions:

* ``npv()`` - Net Present Value calculation
* ``irr()`` - Internal Rate of Return calculation
* ``mirr()`` - Modified Internal Rate of Return
* ``payback_period()`` - Simple payback period calculation
* ``discounted_payback_period()`` - Discounted payback period
* ``profitability_index()`` - Profitability index for investment ranking

Mathematical Foundations
------------------------

All TVM calculations in qfinbox are based on fundamental financial mathematics:

**Present Value Formula:**

.. math::
   PV = \\frac{FV}{(1 + r)^n}

**Future Value Formula:**

.. math::
   FV = PV \\times (1 + r)^n

**Annuity Present Value:**

.. math::
   PV = PMT \\times \\frac{1 - (1 + r)^{-n}}{r}

**Bond Pricing:**

.. math::
   P = \\sum_{t=1}^{n} \\frac{C}{(1 + r)^t} + \\frac{F}{(1 + r)^n}

Where:
- PV = Present Value
- FV = Future Value
- PMT = Payment
- r = Interest Rate per period
- n = Number of periods
- C = Coupon payment
- F = Face value
- P = Bond price

Performance and Accuracy
------------------------

The qfinbox TVM module is optimized for both performance and accuracy:

* **NumPy Integration**: Uses NumPy arrays for vectorized calculations
* **SciPy Optimization**: Leverages SciPy for complex root-finding (IRR, yield calculations)
* **Input Validation**: Comprehensive validation prevents calculation errors
* **Error Handling**: Graceful handling of edge cases and invalid inputs
* **Type Safety**: Full type hints for IDE support and runtime checking

Usage Patterns
--------------

**Single Value Calculations:**

.. code-block:: python

    from qfinbox.tvm import basic

    pv = basic.present_value(fv=1000, rate=0.05, periods=10)

**Array-based Calculations:**

.. code-block:: python

    import numpy as np
    from qfinbox.tvm import basic

    # Calculate PV for multiple scenarios
    fv_values = np.array([1000, 2000, 3000])
    rates = np.array([0.05, 0.06, 0.07])
    periods = np.array([5, 10, 15])

    pv_results = basic.present_value(fv=fv_values, rate=rates, periods=periods)

**Complex Financial Modeling:**

.. code-block:: python

    from qfinbox.tvm import cashflow, loans

    # Combine multiple TVM functions for complex analysis
    principal = 100000
    rate = 0.05/12
    periods = 30*12

    payment = loans.loan_payment(principal, rate, periods)

    # Create cash flow stream for NPV analysis
    cash_flows = [-principal] + [payment] * periods
    npv = cashflow.npv(rate=0.06/12, cash_flows=cash_flows)
