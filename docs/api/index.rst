API Reference
=============

This section provides detailed documentation for all qfinbox modules and functions.

.. toctree::
   :maxdepth: 3

   modules
   tvm

Main Package
------------

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox

Core Modules
------------

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.core.exceptions
   qfinbox.core.validators
   qfinbox.core.utils

Time Value of Money (TVM) Module
--------------------------------

The TVM module provides comprehensive financial calculations across five specialized submodules:

Basic TVM Calculations
~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.basic.present_value
   qfinbox.tvm.basic.future_value
   qfinbox.tvm.basic.interest_rate
   qfinbox.tvm.basic.number_of_periods
   qfinbox.tvm.basic.effective_rate
   qfinbox.tvm.basic.nominal_rate

Annuities
~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.annuities.pv_ordinary_annuity
   qfinbox.tvm.annuities.fv_ordinary_annuity
   qfinbox.tvm.annuities.pv_annuity_due
   qfinbox.tvm.annuities.fv_annuity_due
   qfinbox.tvm.annuities.perpetuity_value
   qfinbox.tvm.annuities.growing_annuity_pv
   qfinbox.tvm.annuities.growing_perpetuity_value

Bond Valuation
~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.bonds.bond_price
   qfinbox.tvm.bonds.bond_yield
   qfinbox.tvm.bonds.bond_duration
   qfinbox.tvm.bonds.bond_convexity
   qfinbox.tvm.bonds.zero_coupon_bond_price
   qfinbox.tvm.bonds.zero_coupon_bond_yield

Loan Analysis
~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.loans.loan_payment
   qfinbox.tvm.loans.loan_balance
   qfinbox.tvm.loans.amortization_schedule
   qfinbox.tvm.loans.total_interest_paid
   qfinbox.tvm.loans.loan_affordability

Cash Flow Analysis
~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.cashflow.npv
   qfinbox.tvm.cashflow.irr
   qfinbox.tvm.cashflow.mirr
   qfinbox.tvm.cashflow.payback_period
   qfinbox.tvm.cashflow.discounted_payback_period
   qfinbox.tvm.cashflow.profitability_index

Module Overview
---------------

The qfinbox library provides a comprehensive suite of financial calculation tools:

* **28+ TVM Functions**: Complete implementation across 5 specialized modules
* **Robust Validation**: Input validation and error handling for all functions
* **Type Safety**: Full type hints and runtime type checking
* **Performance Optimized**: Uses NumPy and SciPy for fast calculations

.. note::
   This API documentation is automatically generated from the source code docstrings.
   All functions include detailed parameter descriptions, return values, and usage examples.
