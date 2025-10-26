"""Basic Time Value of Money calculations."""

import math

from ..core.validators import validate_positive


def future_value(
    present_value: float,
    rate: float,
    periods: int,
    compounding_frequency: int = 1,
) -> float:
    """
    Calculate future value of a present amount.

    Parameters
    ----------
    present_value : float
        Present value amount.
    rate : float
        Annual interest rate (as decimal, e.g., 0.05 for 5%).
    periods : int
        Number of periods.
    compounding_frequency : int, default 1
        Number of times interest is compounded per period.

    Returns
    -------
    float
        Future value.

    Raises
    ------
    ValidationError
        If any parameter is invalid.

    Examples
    --------
    >>> future_value(1000, 0.05, 10)
    1628.89
    """
    validate_positive(present_value, "present_value")
    validate_positive(rate, "rate")
    validate_positive(periods, "periods")
    validate_positive(compounding_frequency, "compounding_frequency")

    return present_value * (1 + rate / compounding_frequency) ** (
        compounding_frequency * periods
    )


def present_value(
    future_value: float,
    rate: float,
    periods: int,
    compounding_frequency: int = 1,
) -> float:
    """
    Calculate present value of a future amount.

    Parameters
    ----------
    future_value : float
        Future value amount.
    rate : float
        Annual interest rate (as decimal).
    periods : int
        Number of periods.
    compounding_frequency : int, default 1
        Number of times interest is compounded per period.

    Returns
    -------
    float
        Present value.

    Examples
    --------
    >>> present_value(1628.89, 0.05, 10)
    1000.0
    """
    validate_positive(future_value, "future_value")
    validate_positive(rate, "rate")
    validate_positive(periods, "periods")
    validate_positive(compounding_frequency, "compounding_frequency")

    return future_value / (1 + rate / compounding_frequency) ** (
        compounding_frequency * periods
    )


def compound_interest(
    principal: float,
    rate: float,
    periods: int,
    compounding_frequency: int = 1,
) -> float:
    """
    Calculate compound interest earned.

    Parameters
    ----------
    principal : float
        Initial principal amount.
    rate : float
        Annual interest rate (as decimal).
    periods : int
        Number of periods.
    compounding_frequency : int, default 1
        Number of times interest is compounded per period.

    Returns
    -------
    float
        Compound interest earned.

    Examples
    --------
    >>> compound_interest(1000, 0.05, 10)
    628.89
    """
    fv = future_value(principal, rate, periods, compounding_frequency)
    return fv - principal


def effective_rate(nominal_rate: float, compounding_frequency: int) -> float:
    """
    Calculate effective annual rate from nominal rate.

    Parameters
    ----------
    nominal_rate : float
        Nominal annual interest rate (as decimal).
    compounding_frequency : int
        Number of compounding periods per year.

    Returns
    -------
    float
        Effective annual rate.

    Examples
    --------
    >>> effective_rate(0.12, 12)  # 12% compounded monthly
    0.1268
    """
    validate_positive(nominal_rate, "nominal_rate")
    validate_positive(compounding_frequency, "compounding_frequency")

    return (1 + nominal_rate / compounding_frequency) ** compounding_frequency - 1


def nominal_rate(effective_rate: float, compounding_frequency: int) -> float:
    """
    Calculate nominal rate from effective annual rate.

    Parameters
    ----------
    effective_rate : float
        Effective annual interest rate (as decimal).
    compounding_frequency : int
        Number of compounding periods per year.

    Returns
    -------
    float
        Nominal annual rate.

    Examples
    --------
    >>> nominal_rate(0.1268, 12)  # Effective 12.68% compounded monthly
    0.12
    """
    validate_positive(effective_rate, "effective_rate")
    validate_positive(compounding_frequency, "compounding_frequency")

    return compounding_frequency * (
        (1 + effective_rate) ** (1 / compounding_frequency) - 1
    )


def continuous_compounding_fv(
    present_value: float,
    rate: float,
    time: float,
) -> float:
    """
    Calculate future value with continuous compounding.

    Parameters
    ----------
    present_value : float
        Present value amount.
    rate : float
        Annual interest rate (as decimal).
    time : float
        Time period in years.

    Returns
    -------
    float
        Future value with continuous compounding.

    Examples
    --------
    >>> continuous_compounding_fv(1000, 0.05, 10)
    1648.72
    """
    validate_positive(present_value, "present_value")
    validate_positive(rate, "rate")
    validate_positive(time, "time")

    return present_value * math.exp(rate * time)


def continuous_compounding_pv(
    future_value: float,
    rate: float,
    time: float,
) -> float:
    """
    Calculate present value with continuous compounding.

    Parameters
    ----------
    future_value : float
        Future value amount.
    rate : float
        Annual interest rate (as decimal).
    time : float
        Time period in years.

    Returns
    -------
    float
        Present value with continuous compounding.

    Examples
    --------
    >>> continuous_compounding_pv(1648.72, 0.05, 10)
    1000.0
    """
    validate_positive(future_value, "future_value")
    validate_positive(rate, "rate")
    validate_positive(time, "time")

    return future_value * math.exp(-rate * time)
