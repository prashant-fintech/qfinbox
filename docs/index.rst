Welcome to qfinbox documentation!
====================================

**qfinbox** is a comprehensive Python library for quantitative finance, providing robust tools for
financial calculations, risk management, and investment analysis. The library is designed for
finance professionals, researchers, and developers who need reliable quantitative finance tools.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   tutorial
   api/index
   examples/index
   contributing
   changelog

Key Features
------------

qfinbox provides a comprehensive suite of financial calculation tools:

* **Time Value of Money (TVM)**: Complete implementation with 28+ functions

  * **Basic Calculations**: Present value, future value, interest rates, and time periods
  * **Annuities**: Ordinary and due annuities, perpetuities, growing annuities
  * **Bond Valuation**: Pricing, yield calculations, duration, and convexity
  * **Loan Analysis**: Payment calculations, amortization schedules, refinancing analysis
  * **Cash Flow Analysis**: NPV, IRR, modified IRR, payback period, profitability index

* **Core Utilities**: Robust validation, error handling, and mathematical utilities
* **Professional API**: Clean, well-documented interface with comprehensive type hints
* **High Performance**: Optimized calculations using NumPy and SciPy

Current Implementation Status
-----------------------------

✅ **Complete TVM Module** (v0.1.0)

* 28+ financial functions across 5 specialized modules
* Comprehensive input validation and error handling
* Full test coverage and documentation
* **Available on PyPI**: ``pip install qfinbox``

Future Roadmap
--------------

* **Risk Management**: VaR, CVaR, stress testing, and scenario analysis
* **Portfolio Optimization**: Modern portfolio theory, efficient frontier, asset allocation
* **Options Pricing**: Black-Scholes, binomial trees, Monte Carlo methods
* **Fixed Income**: Yield curve modeling, duration matching, immunization strategies
* **Market Data Integration**: Real-time data feeds and historical analysis

Quick Installation
------------------

Install qfinbox using pip:

.. code-block:: bash

    pip install qfinbox

Or install from source:

.. code-block:: bash

    git clone https://github.com/prashant-fintech/qfinbox.git
    cd qfinbox
    pip install -e .

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
