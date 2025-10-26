Installation
============

Requirements
------------

qfinbox requires Python 3.8 or higher. The current minimal version has basic dependencies:

* numpy >= 1.21.0
* pandas >= 1.5.0

Install from PyPI
-----------------

.. note::
   qfinbox is currently in development and may not be available on PyPI yet.

Once published, you can install qfinbox using pip:

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
