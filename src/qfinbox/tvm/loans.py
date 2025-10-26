"""Loan calculations and amortization."""

import pandas as pd

from ..core.validators import validate_positive


def loan_payment(
    principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> float:
    """
    Calculate periodic loan payment.

    Parameters
    ----------
    principal : float
        Loan principal amount.
    annual_rate : float
        Annual interest rate (as decimal).
    years : float
        Loan term in years.
    payments_per_year : int, default 12
        Number of payments per year.

    Returns
    -------
    float
        Periodic payment amount.

    Examples
    --------
    >>> loan_payment(300000, 0.05, 30)
    1610.46
    """
    validate_positive(principal, "principal")
    validate_positive(annual_rate, "annual_rate")
    validate_positive(years, "years")
    validate_positive(payments_per_year, "payments_per_year")

    rate_per_period = annual_rate / payments_per_year
    num_payments = years * payments_per_year

    if rate_per_period == 0:
        return principal / num_payments

    return (
        principal
        * (rate_per_period * (1 + rate_per_period) ** num_payments)
        / ((1 + rate_per_period) ** num_payments - 1)
    )


def loan_balance(
    principal: float,
    annual_rate: float,
    years: float,
    payments_made: int,
    payments_per_year: int = 12,
) -> float:
    """
    Calculate remaining loan balance after specified payments.

    Parameters
    ----------
    principal : float
        Original loan principal amount.
    annual_rate : float
        Annual interest rate (as decimal).
    years : float
        Loan term in years.
    payments_made : int
        Number of payments already made.
    payments_per_year : int, default 12
        Number of payments per year.

    Returns
    -------
    float
        Remaining loan balance.

    Examples
    --------
    >>> loan_balance(300000, 0.05, 30, 120)
    260108.58
    """
    validate_positive(principal, "principal")
    validate_positive(annual_rate, "annual_rate")
    validate_positive(years, "years")
    validate_positive(payments_made, "payments_made")
    validate_positive(payments_per_year, "payments_per_year")

    rate_per_period = annual_rate / payments_per_year
    total_payments = years * payments_per_year

    if payments_made >= total_payments:
        return 0.0

    payment = loan_payment(principal, annual_rate, years, payments_per_year)

    if rate_per_period == 0:
        return principal - (payment * payments_made)

    remaining_payments = total_payments - payments_made
    return (
        payment * (1 - (1 + rate_per_period) ** -remaining_payments) / rate_per_period
    )


def total_interest_paid(
    principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> float:
    """
    Calculate total interest paid over the life of the loan.

    Parameters
    ----------
    principal : float
        Loan principal amount.
    annual_rate : float
        Annual interest rate (as decimal).
    years : float
        Loan term in years.
    payments_per_year : int, default 12
        Number of payments per year.

    Returns
    -------
    float
        Total interest paid.

    Examples
    --------
    >>> total_interest_paid(300000, 0.05, 30)
    279767.35
    """
    payment = loan_payment(principal, annual_rate, years, payments_per_year)
    total_payments = years * payments_per_year
    return (payment * total_payments) - principal


def amortization_schedule(
    principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> pd.DataFrame:
    """
    Generate loan amortization schedule.

    Parameters
    ----------
    principal : float
        Loan principal amount.
    annual_rate : float
        Annual interest rate (as decimal).
    years : float
        Loan term in years.
    payments_per_year : int, default 12
        Number of payments per year.

    Returns
    -------
    pd.DataFrame
        Amortization schedule with columns: Payment, Interest, Principal, Balance.

    Examples
    --------
    >>> schedule = amortization_schedule(300000, 0.05, 30)
    >>> schedule.head()
       Payment  Interest   Principal      Balance
    0  1610.46   1250.00     360.46   299639.54
    1  1610.46   1248.50     361.96   299277.58
    """
    validate_positive(principal, "principal")
    validate_positive(annual_rate, "annual_rate")
    validate_positive(years, "years")
    validate_positive(payments_per_year, "payments_per_year")

    rate_per_period = annual_rate / payments_per_year
    total_payments = int(years * payments_per_year)
    payment = loan_payment(principal, annual_rate, years, payments_per_year)

    schedule = []
    balance = principal

    for _ in range(1, total_payments + 1):
        interest_payment = balance * rate_per_period
        principal_payment = payment - interest_payment
        balance -= principal_payment

        # Ensure balance doesn't go negative due to rounding
        if balance < 0:
            principal_payment += balance
            balance = 0

        schedule.append(
            {
                "Payment": payment,
                "Interest": interest_payment,
                "Principal": principal_payment,
                "Balance": balance,
            }
        )

        if balance == 0:
            break

    return pd.DataFrame(schedule)
