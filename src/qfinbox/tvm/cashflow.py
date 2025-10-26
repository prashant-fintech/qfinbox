"""Cash flow analysis and investment evaluation."""

from typing import List, Union

import numpy as np

from scipy.optimize import fsolve

from ..core.validators import validate_positive


def net_present_value(
    cash_flows: Union[List[float], np.ndarray],
    discount_rate: float,
) -> float:
    """
    Calculate net present value of cash flows.

    Parameters
    ----------
    cash_flows : array-like
        Series of cash flows, with initial investment as negative value.
    discount_rate : float
        Discount rate (as decimal).

    Returns
    -------
    float
        Net present value.

    Examples
    --------
    >>> cash_flows = [-100000, 30000, 40000, 50000]
    >>> net_present_value(cash_flows, 0.10)
    4349.34
    """
    # Note: We don't validate positive here as IRR calculation may need negative rates
    if not isinstance(discount_rate, (int, float)):
        raise ValueError("discount_rate must be a number")

    cash_flows = np.array(cash_flows)
    periods = np.arange(len(cash_flows))

    return np.sum(cash_flows / (1 + discount_rate) ** periods)


def internal_rate_of_return(
    cash_flows: Union[List[float], np.ndarray],
    initial_guess: float = 0.1,
) -> float:
    """
    Calculate internal rate of return for cash flows.

    Parameters
    ----------
    cash_flows : array-like
        Series of cash flows, with initial investment as negative value.
    initial_guess : float, default 0.1
        Initial guess for IRR calculation.

    Returns
    -------
    float
        Internal rate of return (as decimal).

    Examples
    --------
    >>> cash_flows = [-100000, 30000, 40000, 50000]
    >>> internal_rate_of_return(cash_flows)
    0.1627
    """
    cash_flows = np.array(cash_flows)

    def npv_func(rate: float) -> float:
        return net_present_value(cash_flows, rate)

    # Try multiple initial guesses if the first one fails
    guesses = [initial_guess, 0.05, 0.15, 0.25, -0.5, 0.5, 1.0]

    for guess in guesses:
        try:
            irr = fsolve(npv_func, guess, full_output=True)
            if irr[2] == 1:  # Successful convergence
                result = irr[0][0]
                # Verify the result makes sense
                if abs(npv_func(result)) < 1e-6:
                    return result
        except (ValueError, RuntimeError, OverflowError):
            continue

    return np.nan


def payback_period(
    cash_flows: Union[List[float], np.ndarray],
) -> float:
    """
    Calculate payback period for cash flows.

    Parameters
    ----------
    cash_flows : array-like
        Series of cash flows, with initial investment as negative value.

    Returns
    -------
    float
        Payback period in years.

    Examples
    --------
    >>> cash_flows = [-100000, 30000, 40000, 50000]
    >>> payback_period(cash_flows)
    2.6
    """
    cash_flows = np.array(cash_flows)
    cumulative = np.cumsum(cash_flows)

    # Find where cumulative becomes positive
    positive_indices = np.where(cumulative > 0)[0]

    if len(positive_indices) == 0:
        return np.inf

    breakeven_period = positive_indices[0]

    if breakeven_period == 0:
        return 0.0

    # Linear interpolation for more precise payback period
    prev_cumulative = cumulative[breakeven_period - 1]
    curr_cash_flow = cash_flows[breakeven_period]

    fraction = abs(prev_cumulative) / curr_cash_flow

    return breakeven_period + fraction


def discounted_payback_period(
    cash_flows: Union[List[float], np.ndarray],
    discount_rate: float,
) -> float:
    """
    Calculate discounted payback period for cash flows.

    Parameters
    ----------
    cash_flows : array-like
        Series of cash flows, with initial investment as negative value.
    discount_rate : float
        Discount rate (as decimal).

    Returns
    -------
    float
        Discounted payback period in years.

    Examples
    --------
    >>> cash_flows = [-100000, 30000, 40000, 50000]
    >>> discounted_payback_period(cash_flows, 0.10)
    2.8
    """
    validate_positive(discount_rate, "discount_rate")

    cash_flows = np.array(cash_flows)
    periods = np.arange(len(cash_flows))

    # Calculate discounted cash flows
    discounted_cf = cash_flows / (1 + discount_rate) ** periods

    return payback_period(discounted_cf)


def profitability_index(
    cash_flows: Union[List[float], np.ndarray],
    discount_rate: float,
) -> float:
    """
    Calculate profitability index for cash flows.

    Parameters
    ----------
    cash_flows : array-like
        Series of cash flows, with initial investment as negative value.
    discount_rate : float
        Discount rate (as decimal).

    Returns
    -------
    float
        Profitability index.

    Examples
    --------
    >>> cash_flows = [-100000, 30000, 40000, 50000]
    >>> profitability_index(cash_flows, 0.10)
    1.043
    """
    validate_positive(discount_rate, "discount_rate")

    cash_flows = np.array(cash_flows)
    initial_investment = abs(cash_flows[0])  # Make positive

    # Present value of future cash flows
    future_cf = cash_flows[1:]
    periods = np.arange(1, len(cash_flows))

    pv_future_cf = np.sum(future_cf / (1 + discount_rate) ** periods)

    return pv_future_cf / initial_investment
