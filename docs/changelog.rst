Changelog
=========

All notable changes to qfinbox will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Added
~~~~~
- Enhanced documentation with comprehensive examples and tutorials
- Advanced TVM usage patterns and real-world scenarios
- Performance optimization tips and best practices

[0.1.0] - 2025-10-26
---------------------

Added
~~~~~

**Complete Time Value of Money (TVM) Implementation** - The flagship feature of qfinbox v0.1.0

- **Core TVM Module** with 28+ financial functions across 5 specialized modules:

  - ``qfinbox.tvm.basic``: Present/future value, interest rates, compounding (6 functions)
  - ``qfinbox.tvm.annuities``: Ordinary/due annuities, perpetuities, growing annuities (7 functions)
  - ``qfinbox.tvm.bonds``: Bond pricing, yield, duration, convexity analysis (6 functions)
  - ``qfinbox.tvm.loans``: Payment calculations, amortization schedules, loan analysis (5 functions)
  - ``qfinbox.tvm.cashflow``: NPV, IRR, payback period, profitability analysis (6 functions)

- **Robust Core Infrastructure**:

  - ``qfinbox.core.validators``: Comprehensive input validation and type checking
  - ``qfinbox.core.exceptions``: Custom financial calculation exceptions
  - ``qfinbox.core.utils``: Mathematical utilities and helper functions

- **Professional Package Features**:

  - Modern Python packaging with ``pyproject.toml``
  - Full type hints and runtime type checking
  - Comprehensive error handling and input validation
  - NumPy and SciPy integration for performance
  - Extensive docstrings with usage examples

- **Complete Documentation Suite**:

  - Comprehensive API reference with auto-generated docs
  - Step-by-step tutorial covering all TVM concepts
  - Real-world examples and practical scenarios
  - Installation and quick start guides
  - Mathematical foundations and formula references

- **Development Infrastructure**:

  - Modern Python packaging and distribution
  - Black code formatting and isort import sorting
  - Type checking with mypy and comprehensive validation
  - Test suite with pytest framework
  - Continuous integration ready

- **PyPI Distribution**:

  - Published to Python Package Index (PyPI)
  - Easy installation with ``pip install qfinbox``
  - Professional distribution with proper metadata
  - Comprehensive README with badges and examples

**Key TVM Functions Include**:

- **Basic calculations**: ``present_value()``, ``future_value()``, ``interest_rate()``, ``number_of_periods()``
- **Annuity calculations**: ``pv_ordinary_annuity()``, ``fv_annuity_due()``, ``perpetuity_value()``
- **Bond analysis**: ``bond_price()``, ``bond_yield()``, ``bond_duration()``, ``bond_convexity()``
- **Loan analysis**: ``loan_payment()``, ``amortization_schedule()``, ``loan_balance()``
- **Investment analysis**: ``npv()``, ``irr()``, ``mirr()``, ``payback_period()``, ``profitability_index()``

Changed
~~~~~~~
- N/A (Initial release)

Deprecated
~~~~~~~~~~
- N/A (Initial release)

Removed
~~~~~~~
- N/A (Initial release)

Fixed
~~~~~
- N/A (Initial release)

Security
~~~~~~~~
- N/A (Initial release)
