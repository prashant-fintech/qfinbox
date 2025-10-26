"""Bond valuation and analysis."""

from scipy.optimize import brentq

from ..core.validators import validate_positive


def bond_price(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: float,
    yield_to_maturity: float,
    payments_per_year: int = 2,
) -> float:
    """
    Calculate bond price given yield to maturity.

    Parameters
    ----------
    face_value : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate (as decimal).
    years_to_maturity : float
        Years until maturity.
    yield_to_maturity : float
        Yield to maturity (as decimal).
    payments_per_year : int, default 2
        Number of coupon payments per year.

    Returns
    -------
    float
        Bond price.

    Examples
    --------
    >>> bond_price(1000, 0.06, 10, 0.08)
    864.10
    """
    validate_positive(face_value, "face_value")
    validate_positive(coupon_rate, "coupon_rate")
    validate_positive(years_to_maturity, "years_to_maturity")
    validate_positive(yield_to_maturity, "yield_to_maturity")
    validate_positive(payments_per_year, "payments_per_year")

    periods = int(years_to_maturity * payments_per_year)
    coupon_payment = face_value * coupon_rate / payments_per_year
    discount_rate = yield_to_maturity / payments_per_year

    # Present value of coupon payments
    pv_coupons = coupon_payment * (1 - (1 + discount_rate) ** -periods) / discount_rate

    # Present value of face value
    pv_face = face_value / (1 + discount_rate) ** periods

    return pv_coupons + pv_face


def bond_yield_to_maturity(
    price: float,
    face_value: float,
    coupon_rate: float,
    years_to_maturity: float,
    payments_per_year: int = 2,
) -> float:
    """
    Calculate bond yield to maturity given price.

    Parameters
    ----------
    price : float
        Current bond price.
    face_value : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate (as decimal).
    years_to_maturity : float
        Years until maturity.
    payments_per_year : int, default 2
        Number of coupon payments per year.

    Returns
    -------
    float
        Yield to maturity (as decimal).

    Examples
    --------
    >>> bond_yield_to_maturity(864.10, 1000, 0.06, 10)
    0.08
    """
    validate_positive(price, "price")
    validate_positive(face_value, "face_value")
    validate_positive(coupon_rate, "coupon_rate")
    validate_positive(years_to_maturity, "years_to_maturity")
    validate_positive(payments_per_year, "payments_per_year")

    def price_diff(ytm: float) -> float:
        return (
            bond_price(
                face_value, coupon_rate, years_to_maturity, ytm, payments_per_year
            )
            - price
        )

    # Use numerical method to find YTM
    return brentq(price_diff, 0.001, 1.0)


def bond_duration(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: float,
    yield_to_maturity: float,
    payments_per_year: int = 2,
) -> float:
    """
    Calculate Macaulay duration of a bond.

    Parameters
    ----------
    face_value : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate (as decimal).
    years_to_maturity : float
        Years until maturity.
    yield_to_maturity : float
        Yield to maturity (as decimal).
    payments_per_year : int, default 2
        Number of coupon payments per year.

    Returns
    -------
    float
        Macaulay duration in years.

    Examples
    --------
    >>> bond_duration(1000, 0.06, 10, 0.08)
    7.25
    """
    validate_positive(face_value, "face_value")
    validate_positive(coupon_rate, "coupon_rate")
    validate_positive(years_to_maturity, "years_to_maturity")
    validate_positive(yield_to_maturity, "yield_to_maturity")
    validate_positive(payments_per_year, "payments_per_year")

    periods = int(years_to_maturity * payments_per_year)
    coupon_payment = face_value * coupon_rate / payments_per_year
    discount_rate = yield_to_maturity / payments_per_year

    bond_px = bond_price(
        face_value, coupon_rate, years_to_maturity, yield_to_maturity, payments_per_year
    )

    weighted_time = 0
    for t in range(1, int(periods) + 1):
        if t < periods:
            cash_flow = coupon_payment
        else:
            cash_flow = coupon_payment + face_value

        pv_cash_flow = cash_flow / (1 + discount_rate) ** t
        weight = pv_cash_flow / bond_px
        weighted_time += weight * (t / payments_per_year)

    return weighted_time


def bond_modified_duration(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: float,
    yield_to_maturity: float,
    payments_per_year: int = 2,
) -> float:
    """
    Calculate modified duration of a bond.

    Parameters
    ----------
    face_value : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate (as decimal).
    years_to_maturity : float
        Years until maturity.
    yield_to_maturity : float
        Yield to maturity (as decimal).
    payments_per_year : int, default 2
        Number of coupon payments per year.

    Returns
    -------
    float
        Modified duration.

    Examples
    --------
    >>> bond_modified_duration(1000, 0.06, 10, 0.08)
    6.71
    """
    mac_duration = bond_duration(
        face_value, coupon_rate, years_to_maturity, yield_to_maturity, payments_per_year
    )
    return mac_duration / (1 + yield_to_maturity / payments_per_year)


def bond_convexity(
    face_value: float,
    coupon_rate: float,
    years_to_maturity: float,
    yield_to_maturity: float,
    payments_per_year: int = 2,
) -> float:
    """
    Calculate convexity of a bond.

    Parameters
    ----------
    face_value : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate (as decimal).
    years_to_maturity : float
        Years until maturity.
    yield_to_maturity : float
        Yield to maturity (as decimal).
    payments_per_year : int, default 2
        Number of coupon payments per year.

    Returns
    -------
    float
        Convexity.

    Examples
    --------
    >>> bond_convexity(1000, 0.06, 10, 0.08)
    64.93
    """
    validate_positive(face_value, "face_value")
    validate_positive(coupon_rate, "coupon_rate")
    validate_positive(years_to_maturity, "years_to_maturity")
    validate_positive(yield_to_maturity, "yield_to_maturity")
    validate_positive(payments_per_year, "payments_per_year")

    periods = int(years_to_maturity * payments_per_year)
    coupon_payment = face_value * coupon_rate / payments_per_year
    discount_rate = yield_to_maturity / payments_per_year

    bond_px = bond_price(
        face_value, coupon_rate, years_to_maturity, yield_to_maturity, payments_per_year
    )

    convexity = 0
    for t in range(1, int(periods) + 1):
        if t < periods:
            cash_flow = coupon_payment
        else:
            cash_flow = coupon_payment + face_value

        pv_cash_flow = cash_flow / (1 + discount_rate) ** t
        convexity += (pv_cash_flow * t * (t + 1)) / ((1 + discount_rate) ** 2)

    return convexity / bond_px
