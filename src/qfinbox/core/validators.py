"""Input validation utilities for qfinbox."""

from typing import Union

import numpy as np
import pandas as pd

from .exceptions import ValidationError


def validate_weights(weights: Union[np.ndarray, pd.Series, list]) -> np.ndarray:
    """
    Validate portfolio weights.

    Parameters
    ----------
    weights : array-like
        Portfolio weights to validate.

    Returns
    -------
    np.ndarray
        Validated weights as numpy array.

    Raises
    ------
    ValidationError
        If weights are invalid.
    """
    weights = np.asarray(weights, dtype=float)

    if len(weights) == 0:
        raise ValidationError("Weights cannot be empty")

    if np.any(np.isnan(weights)):
        raise ValidationError("Weights cannot contain NaN values")

    if not np.isclose(np.sum(weights), 1.0, atol=1e-6):
        raise ValidationError("Weights must sum to 1.0")

    return weights


def validate_returns(returns: Union[np.ndarray, pd.Series, pd.DataFrame]) -> np.ndarray:
    """
    Validate return data.

    Parameters
    ----------
    returns : array-like
        Return data to validate.

    Returns
    -------
    np.ndarray
        Validated returns as numpy array.

    Raises
    ------
    ValidationError
        If returns are invalid.
    """
    returns = np.asarray(returns, dtype=float)

    if returns.size == 0:
        raise ValidationError("Returns cannot be empty")

    if np.any(np.isnan(returns)):
        raise ValidationError("Returns cannot contain NaN values")

    return returns


def validate_positive(value: float, name: str = "value") -> float:
    """
    Validate that a value is positive.

    Parameters
    ----------
    value : float
        Value to validate.
    name : str, default "value"
        Name of the parameter for error messages.

    Returns
    -------
    float
        The validated value.

    Raises
    ------
    ValidationError
        If value is not positive.
    """
    if not isinstance(value, (int, float)):
        raise ValidationError(f"{name} must be a number")

    if value <= 0:
        raise ValidationError(f"{name} must be positive")

    return float(value)
