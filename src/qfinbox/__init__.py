"""
qfinbox: A Python library for quantitative finance.

qfinbox provides tools for risk management, portfolio optimization,
and financial modeling. It enables easy simulation of market scenarios
and investment strategy optimization, enhancing financial analysis
and decision-making.
"""

from . import tvm
from ._version import __version__
from .core import (
    CalculationError,
    DataError,
    QFinBoxError,
    ValidationError,
    calculate_annualized_return,
    calculate_annualized_volatility,
    ensure_1d,
    ensure_2d,
    to_numpy,
    validate_positive,
    validate_returns,
    validate_weights,
)


__author__ = "prashant-fintech"
__email__ = "box_prashant@outlook.com"

# Import main modules when they are created
# from . import risk
# from . import portfolio
# from . import models
# from . import simulation
# from . import data
# from . import analysis
# from . import backtest
# from . import utils

__all__ = [
    "CalculationError",
    "DataError",
    "QFinBoxError",
    "ValidationError",
    "__author__",
    "__email__",
    "__version__",
    "calculate_annualized_return",
    "calculate_annualized_volatility",
    "ensure_1d",
    "ensure_2d",
    "to_numpy",
    "tvm",
    "validate_positive",
    "validate_returns",
    "validate_weights",
    # Add module names as they are implemented
    # "risk",
    # "portfolio",
    # "models",
    # "simulation",
    # "data",
    # "analysis",
    # "backtest",
    # "utils",
]
