"""Annuity calculations."""

from ..core.validators import validate_positive


def ordinary_annuity_pv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """
    Calculate present value of ordinary annuity.

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.

    Returns
    -------
    float
        Present value of ordinary annuity.

    Examples
    --------
    >>> ordinary_annuity_pv(1000, 0.05, 10)
    7721.73
    """
    validate_positive(payment, "payment")
    validate_positive(rate, "rate")
    validate_positive(periods, "periods")

    return payment * (1 - (1 + rate) ** -periods) / rate


def ordinary_annuity_fv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """
    Calculate future value of ordinary annuity.

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.

    Returns
    -------
    float
        Future value of ordinary annuity.

    Examples
    --------
    >>> ordinary_annuity_fv(1000, 0.05, 10)
    12577.89
    """
    validate_positive(payment, "payment")
    validate_positive(rate, "rate")
    validate_positive(periods, "periods")

    return payment * (((1 + rate) ** periods - 1) / rate)


def annuity_due_pv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """
    Calculate present value of annuity due.

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.

    Returns
    -------
    float
        Present value of annuity due.

    Examples
    --------
    >>> annuity_due_pv(1000, 0.05, 10)
    8107.82
    """
    return ordinary_annuity_pv(payment, rate, periods) * (1 + rate)


def annuity_due_fv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """
    Calculate future value of annuity due.

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.

    Returns
    -------
    float
        Future value of annuity due.

    Examples
    --------
    >>> annuity_due_fv(1000, 0.05, 10)
    13206.79
    """
    return ordinary_annuity_fv(payment, rate, periods) * (1 + rate)


def annuity_pv(
    payment: float,
    rate: float,
    periods: int,
    due: bool = False,
) -> float:
    """
    Calculate present value of annuity (ordinary or due).

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.
    due : bool, default False
        If True, calculate annuity due. If False, ordinary annuity.

    Returns
    -------
    float
        Present value of annuity.
    """
    if due:
        return annuity_due_pv(payment, rate, periods)
    return ordinary_annuity_pv(payment, rate, periods)


def annuity_fv(
    payment: float,
    rate: float,
    periods: int,
    due: bool = False,
) -> float:
    """
    Calculate future value of annuity (ordinary or due).

    Parameters
    ----------
    payment : float
        Periodic payment amount.
    rate : float
        Interest rate per period (as decimal).
    periods : int
        Number of periods.
    due : bool, default False
        If True, calculate annuity due. If False, ordinary annuity.

    Returns
    -------
    float
        Future value of annuity.
    """
    if due:
        return annuity_due_fv(payment, rate, periods)
    return ordinary_annuity_fv(payment, rate, periods)
