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
   qfinbox.tvm.basic.effective_rate
   qfinbox.tvm.basic.nominal_rate

Annuities
~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.annuities.ordinary_annuity_pv
   qfinbox.tvm.annuities.ordinary_annuity_fv
   qfinbox.tvm.annuities.annuity_due_pv
   qfinbox.tvm.annuities.annuity_due_fv
   qfinbox.tvm.annuities.annuity_pv
   qfinbox.tvm.annuities.annuity_fv

Bond Valuation
~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.bonds.bond_price
   qfinbox.tvm.bonds.bond_yield_to_maturity
   qfinbox.tvm.bonds.bond_duration
   qfinbox.tvm.bonds.bond_modified_duration
   qfinbox.tvm.bonds.bond_convexity

Loan Analysis
~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.loans.loan_payment
   qfinbox.tvm.loans.loan_balance
   qfinbox.tvm.loans.amortization_schedule
   qfinbox.tvm.loans.total_interest_paid

Cash Flow Analysis
~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated/
   :nosignatures:

   qfinbox.tvm.cashflow.net_present_value
   qfinbox.tvm.cashflow.internal_rate_of_return
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
