Installation
============

Requirements
------------

qfinbox requires Python 3.8 or higher and depends on several scientific computing libraries:

* numpy >= 1.21.0
* pandas >= 1.3.0
* scipy >= 1.7.0
* matplotlib >= 3.4.0
* seaborn >= 0.11.0
* yfinance >= 0.1.70

Install from PyPI
-----------------

The easiest way to install qfinbox is using pip:

.. code-block:: bash

    pip install qfinbox

Install Development Version
---------------------------

To install the latest development version from GitHub:

.. code-block:: bash

    git clone https://github.com/prashant-fintech/qfinbox.git
    cd qfinbox
    pip install -e .

Optional Dependencies
---------------------

For development work, install with development dependencies:

.. code-block:: bash

    pip install -e .[dev]

For advanced features (machine learning, advanced optimization):

.. code-block:: bash

    pip install -e .[advanced]

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
