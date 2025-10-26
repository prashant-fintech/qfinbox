"""Common utilities for qfinbox."""

from typing import Union

import numpy as np
import pandas as pd


def to_numpy(data: Union[np.ndarray, pd.Series, pd.DataFrame, list]) -> np.ndarray:
    """
    Convert data to numpy array.

    Parameters
    ----------
    data : array-like
        Data to convert.

    Returns
    -------
    np.ndarray
        Data as numpy array.
    """
    return np.asarray(data, dtype=float)


def ensure_1d(data: Union[np.ndarray, pd.Series, list]) -> np.ndarray:
    """
    Ensure data is a 1D numpy array.

    Parameters
    ----------
    data : array-like
        Data to convert.

    Returns
    -------
    np.ndarray
        1D numpy array.

    Raises
    ------
    ValueError
        If data cannot be converted to 1D array.
    """
    arr = to_numpy(data)

    if arr.ndim == 0:
        return arr.reshape(1)
    elif arr.ndim == 1:
        return arr
    elif arr.ndim == 2 and arr.shape[1] == 1:
        return arr.flatten()
    else:
        raise ValueError(
            f"Cannot convert {arr.ndim}D array with shape {arr.shape} to 1D"
        )


def ensure_2d(data: Union[np.ndarray, pd.DataFrame, list]) -> np.ndarray:
    """
    Ensure data is a 2D numpy array.

    Parameters
    ----------
    data : array-like
        Data to convert.

    Returns
    -------
    np.ndarray
        2D numpy array.
    """
    arr = to_numpy(data)

    if arr.ndim == 1:
        return arr.reshape(-1, 1)
    elif arr.ndim == 2:
        return arr
    else:
        return arr.reshape(arr.shape[0], -1)


def calculate_annualized_return(returns: np.ndarray, frequency: int = 252) -> float:
    """
    Calculate annualized return from a series of returns.

    Parameters
    ----------
    returns : np.ndarray
        Array of returns.
    frequency : int, default 252
        Number of periods per year (252 for daily, 12 for monthly).

    Returns
    -------
    float
        Annualized return.
    """
    total_return = np.prod(1 + returns)
    n_periods = len(returns)
    return (total_return ** (frequency / n_periods)) - 1


def calculate_annualized_volatility(returns: np.ndarray, frequency: int = 252) -> float:
    """
    Calculate annualized volatility from a series of returns.

    Parameters
    ----------
    returns : np.ndarray
        Array of returns.
    frequency : int, default 252
        Number of periods per year (252 for daily, 12 for monthly).

    Returns
    -------
    float
        Annualized volatility.
    """
    return np.std(returns, ddof=1) * np.sqrt(frequency)
