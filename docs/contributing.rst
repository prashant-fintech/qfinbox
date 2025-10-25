Contributing
============

We welcome contributions to qfinbox! This document provides guidelines for contributing to the project.

Getting Started
---------------

1. **Fork the Repository**
   
   Fork the qfinbox repository on GitHub and clone your fork locally:

   .. code-block:: bash

       git clone https://github.com/yourusername/qfinbox.git
       cd qfinbox

2. **Set Up Development Environment**

   Install the development dependencies:

   .. code-block:: bash

       pip install -e .[dev]

3. **Create a Feature Branch**

   .. code-block:: bash

       git checkout -b feature/your-feature-name

Development Guidelines
----------------------

Code Style
~~~~~~~~~~

We use several tools to maintain code quality:

* **Black** for code formatting
* **isort** for import sorting  
* **flake8** for linting
* **mypy** for type checking

Run these tools before submitting:

.. code-block:: bash

    # Format code
    black src/ tests/
    isort src/ tests/
    
    # Check linting
    flake8 src/ tests/
    
    # Type checking
    mypy src/

Or use pre-commit hooks:

.. code-block:: bash

    pre-commit install
    pre-commit run --all-files

Testing
~~~~~~~

Write tests for all new functionality:

.. code-block:: bash

    # Run tests
    pytest tests/
    
    # With coverage
    pytest tests/ --cov=qfinbox --cov-report=html

Documentation
~~~~~~~~~~~~~

Update documentation for new features:

* Add docstrings to all public functions and classes
* Follow NumPy/Google docstring style
* Update relevant .rst files in docs/
* Add examples for complex functionality

Commit Guidelines
-----------------

Use clear, descriptive commit messages:

.. code-block::

    feat: add portfolio optimization module
    fix: resolve numerical instability in VaR calculation
    docs: update risk management examples
    test: add tests for Monte Carlo simulation

Types of Contributions
----------------------

Bug Reports
~~~~~~~~~~~

When reporting bugs, please include:

* Clear description of the issue
* Minimal code example to reproduce
* Expected vs actual behavior
* Python version and dependencies
* Error messages and stack traces

Feature Requests
~~~~~~~~~~~~~~~~

For new features, please:

* Describe the use case and motivation
* Provide examples of the proposed API
* Consider performance implications
* Check if similar functionality exists

Code Contributions
~~~~~~~~~~~~~~~~~~

We welcome contributions in these areas:

**Risk Management**
* New risk metrics and models
* Stress testing frameworks
* Regulatory capital calculations

**Portfolio Optimization**
* Alternative optimization algorithms
* Multi-objective optimization
* Transaction cost modeling

**Financial Models**
* Options pricing models
* Fixed income analytics
* Credit risk models

**Data Integration**
* New data source connectors
* Data cleaning utilities
* Market data normalization

**Performance**
* Algorithmic improvements
* Caching mechanisms
* Parallel processing

Code Review Process
-------------------

1. **Submit Pull Request**
   
   Create a pull request with:
   
   * Clear title and description
   * Link to related issues
   * Summary of changes made
   * Testing performed

2. **Code Review**
   
   Maintainers will review for:
   
   * Code quality and style
   * Test coverage
   * Documentation completeness
   * Performance considerations
   * API design consistency

3. **Continuous Integration**
   
   All PRs must pass:
   
   * Unit tests
   * Code quality checks
   * Documentation builds
   * Example notebook execution

Documentation Standards
-----------------------

Docstring Format
~~~~~~~~~~~~~~~~

Use NumPy-style docstrings:

.. code-block:: python

    def calculate_var(returns: np.ndarray, confidence: float = 0.95) -> float:
        """Calculate Value at Risk using historical method.
        
        Parameters
        ----------
        returns : np.ndarray
            Array of historical returns
        confidence : float, default 0.95
            Confidence level for VaR calculation
            
        Returns
        -------
        float
            Value at Risk at specified confidence level
            
        Examples
        --------
        >>> returns = np.random.normal(0, 0.01, 1000)
        >>> var_95 = calculate_var(returns, 0.95)
        >>> print(f"95% VaR: {var_95:.4f}")
        95% VaR: -0.0163
        
        Notes
        -----
        This implementation uses the historical simulation method,
        which makes no assumptions about return distribution.
        
        References
        ----------
        .. [1] Jorion, P. (2007). Value at Risk: The New Benchmark
               for Managing Financial Risk. McGraw-Hill.
        """

Example Guidelines
~~~~~~~~~~~~~~~~~~

When adding examples:

* Use realistic but synthetic data
* Include full working code
* Add explanatory comments
* Show visualization when appropriate
* Provide interpretation of results

Release Process
---------------

qfinbox follows semantic versioning (SemVer):

* **Major** (x.0.0): Breaking API changes
* **Minor** (x.y.0): New features, backward compatible
* **Patch** (x.y.z): Bug fixes, backward compatible

Community Guidelines
--------------------

* Be respectful and inclusive
* Help newcomers get started  
* Share knowledge and expertise
* Provide constructive feedback
* Follow the code of conduct

Getting Help
------------

If you need help:

* Check existing documentation and examples
* Search GitHub issues for similar problems
* Ask questions in GitHub Discussions
* Contact maintainers directly for urgent issues

Recognition
-----------

Contributors are recognized through:

* GitHub contributor list
* Release notes acknowledgments  
* Documentation credits
* Conference presentations (with permission)

Thank You!
----------

Thank you for contributing to qfinbox! Your efforts help make quantitative
finance more accessible to the Python community.