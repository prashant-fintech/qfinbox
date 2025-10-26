Quick Start Guide
==================

This guide will get you up and running with qfinbox's Time Value of Money (TVM) calculations.

Installation
------------

Install qfinbox using pip:

.. code-block:: bash

    pip install qfinbox

Basic Usage
-----------

Here's how to get started with qfinbox TVM calculations:

.. code-block:: python

    import qfinbox as qf
    from qfinbox.tvm import basic, annuities, bonds, loans, cashflow

    # Basic TVM calculations
    pv = basic.present_value(fv=1000, rate=0.05, periods=10)
    print(f"Present Value: ${pv:.2f}")  # Present Value: $613.91

    fv = basic.future_value(pv=1000, rate=0.05, periods=10)
    print(f"Future Value: ${fv:.2f}")   # Future Value: $1628.89

    # Annuity calculations
    pv_annuity = annuities.pv_ordinary_annuity(pmt=100, rate=0.05, periods=10)
    print(f"PV of Annuity: ${pv_annuity:.2f}")  # PV of Annuity: $772.17

    # Bond valuation
    bond_price = bonds.bond_price(face_value=1000, coupon_rate=0.06,
                                  market_rate=0.05, periods=10)
    print(f"Bond Price: ${bond_price:.2f}")      # Bond Price: $1077.22

    # Loan calculations
    payment = loans.loan_payment(principal=100000, rate=0.05, periods=360)
    print(f"Monthly Payment: ${payment:.2f}")    # Monthly Payment: $536.82

    # Cash flow analysis
    cash_flows = [-1000, 300, 400, 500, 600]
    npv = cashflow.npv(rate=0.10, cash_flows=cash_flows)
    print(f"Net Present Value: ${npv:.2f}")      # Net Present Value: $432.84

Next Steps
----------

1. **Explore the API**: Check out the :doc:`api/index` for available functions
2. **Check Examples**: Look at the :doc:`examples/index` for practical use cases
3. **Contribute**: Help build the library on GitHub
4. **Stay Updated**: Watch the repository for new features

Getting Help
------------

* **Documentation**: You're reading it!
* **GitHub Issues**: Report bugs and request features
* **GitHub Repository**: https://github.com/prashant-fintech/qfinbox
