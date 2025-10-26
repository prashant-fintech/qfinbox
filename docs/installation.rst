Installation
============

Requirements
------------

qfinbox requires Python 3.8 or higher and has the following dependencies:

**Core Dependencies:**
* numpy >= 1.21.0 - Numerical computing and array operations
* pandas >= 1.5.0 - Data manipulation and analysis
* scipy >= 1.9.0 - Scientific computing and optimization

**Optional Dependencies:**
* matplotlib >= 3.5.0 - Plotting and visualization (for charts)
* jupyter >= 1.0.0 - Notebook support (for interactive examples)

Install from PyPI
-----------------

qfinbox is available on PyPI and can be installed using pip:

.. code-block:: bash

    pip install qfinbox

**Latest Version:** 0.1.0 (Released: October 26, 2025)

**What's Included:**
* Complete Time Value of Money (TVM) module with 28+ functions
* Basic TVM calculations (present/future value, rates, periods)
* Annuity calculations (ordinary, due, perpetuities, growing)
* Bond valuation (pricing, yield, duration, convexity)
* Loan analysis (payments, balances, amortization schedules)
* Cash flow analysis (NPV, IRR, payback period, profitability index)

Install Development Version
---------------------------

To install the latest development version from GitHub:

.. code-block:: bash

    git clone https://github.com/prashant-fintech/qfinbox.git
    cd qfinbox
    pip install -e .

Optional Dependencies
---------------------

For documentation building:

.. code-block:: bash

    pip install -e .[docs]

Verification
------------

To verify your installation, run:

.. code-block:: python

    import qfinbox
    print(qfinbox.__version__)

Troubleshooting
---------------

If you encounter installation issues:

1. **Update pip**: ``pip install --upgrade pip``
2. **Use conda**: Consider using conda for scientific packages
3. **Virtual environment**: Use a clean virtual environment
4. **System packages**: Some dependencies may require system libraries

Common Issues
~~~~~~~~~~~~~

**Windows Users**: Some packages may require Visual C++ Build Tools.

**macOS Users**: You may need to install Xcode Command Line Tools:

.. code-block:: bash

    xcode-select --install

**Linux Users**: Install development headers for your distribution.
