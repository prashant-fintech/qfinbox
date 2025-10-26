# qfinbox

[![PyPI version](https://badge.fury.io/py/qfinbox.svg)](https://badge.fury.io/py/qfinbox)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/qfinbox/badge/?version=latest)](https://qfinbox.readthedocs.io/en/latest/?badge=latest)

**qfinbox** is a comprehensive Python library for quantitative finance, offering professional-grade tools for risk management, portfolio optimization, and financial modeling. It enables easy simulation of market scenarios and investment strategy optimization, enhancing financial analysis and decision-making.

## ✨ Features

### 🧮 Time Value of Money (TVM)
- **Basic TVM**: Future/present value calculations with various compounding methods
- **Annuities**: Ordinary and due annuities (PV/FV calculations)
- **Bond Valuation**: Pricing, yield-to-maturity, duration, and convexity
- **Loan Analysis**: Payment calculations, amortization schedules, and balance tracking
- **Cash Flow Analysis**: NPV, IRR, payback periods, and profitability index

### 🛡️ Core Utilities
- **Input Validation**: Robust parameter validation for financial calculations
- **Exception Handling**: Custom exception hierarchy for clear error reporting
- **Data Conversion**: Seamless integration with NumPy arrays and Pandas DataFrames
- **Type Safety**: Full type hints throughout the codebase

## 🚀 Installation

```bash
pip install qfinbox
```

For development dependencies:
```bash
pip install qfinbox[dev]
```

For advanced features:
```bash
pip install qfinbox[advanced]
```

## 📋 Requirements

- Python 3.8+
- NumPy >= 1.21.0
- Pandas >= 1.3.0
- SciPy >= 1.7.0

## 🎯 Quick Start

```python
import qfinbox as qf

# Basic TVM calculations
fv = qf.tvm.future_value(1000, 0.05, 10)  # $1,628.89
pv = qf.tvm.present_value(fv, 0.05, 10)   # $1,000.00

# Annuity calculations
annuity_pv = qf.tvm.ordinary_annuity_pv(1000, 0.05, 10)  # $7,721.73
annuity_fv = qf.tvm.ordinary_annuity_fv(1000, 0.05, 10)  # $12,577.89

# Bond valuation
bond_price = qf.tvm.bond_price(1000, 0.06, 10, 0.08)  # $864.10
duration = qf.tvm.bond_duration(1000, 0.06, 10, 0.08)  # 7.45 years

# Loan calculations
monthly_payment = qf.tvm.loan_payment(300000, 0.05, 30, 12)  # $1,610.46
schedule = qf.tvm.amortization_schedule(100000, 0.06, 15, 12)

# Cash flow analysis
cash_flows = [-100000, 30000, 40000, 50000]
npv = qf.tvm.net_present_value(cash_flows, 0.10)  # $-2,103.68
payback = qf.tvm.payback_period(cash_flows)        # 3.6 years

# Input validation and error handling
try:
    weights = qf.validate_weights([0.4, 0.3, 0.3])  # ✓ Valid
    invalid = qf.validate_weights([0.5, 0.3, 0.3])  # ✗ Raises ValidationError
except qf.ValidationError as e:
    print(f"Error: {e}")
```

## 📖 Documentation

Full documentation is available at [https://qfinbox.readthedocs.io](https://qfinbox.readthedocs.io)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏦 Use Cases

- **Investment Analysis**: Calculate returns, risk metrics, and portfolio optimization
- **Loan Analysis**: Mortgage calculations, amortization schedules, and payment planning
- **Bond Valuation**: Price bonds, calculate yields, duration, and convexity
- **Project Finance**: NPV analysis, IRR calculations, and investment decision-making
- **Risk Management**: Portfolio risk assessment and scenario analysis
- **Financial Planning**: Retirement planning, education funding, and goal-based investing

## 🔗 Links

- **Homepage**: [https://github.com/prashant-fintech/qfinbox](https://github.com/prashant-fintech/qfinbox)
- **Documentation**: [https://qfinbox.readthedocs.io](https://qfinbox.readthedocs.io)
- **PyPI**: [https://pypi.org/project/qfinbox/](https://pypi.org/project/qfinbox/)
- **Issues**: [https://github.com/prashant-fintech/qfinbox/issues](https://github.com/prashant-fintech/qfinbox/issues)
