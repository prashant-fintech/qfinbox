"""Test the TVM (Time Value of Money) module functionality."""

import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import numpy as np

import qfinbox as qf


print("Testing qfinbox TVM module...")
print(f"Version: {qf.__version__}")
print(f"TVM module available: {'tvm' in dir(qf)}")

# Test basic TVM functions
print("\n--- Basic TVM Functions ---")
pv = 1000
rate = 0.05
years = 10

fv = qf.tvm.future_value(pv, rate, years)
print(f"Future value of ${pv:,} at {rate*100}% for {years} years: ${fv:,.2f}")

calculated_pv = qf.tvm.present_value(fv, rate, years)
print(
    f"Present value of ${fv:,.2f} at {rate*100}% for {years} years: ${calculated_pv:,.2f}"
)

# Test annuity functions
print("\n--- Annuity Functions ---")
payment = 1000
periods = 10

ann_pv = qf.tvm.ordinary_annuity_pv(payment, rate, periods)
ann_fv = qf.tvm.ordinary_annuity_fv(payment, rate, periods)
print(f"Ordinary annuity PV of ${payment}/period for {periods} periods: ${ann_pv:,.2f}")
print(f"Ordinary annuity FV of ${payment}/period for {periods} periods: ${ann_fv:,.2f}")

# Test bond functions
print("\n--- Bond Functions ---")
face_value = 1000
coupon_rate = 0.06
maturity_years = 10
ytm = 0.08

bond_px = qf.tvm.bond_price(face_value, coupon_rate, maturity_years, ytm)
duration = qf.tvm.bond_duration(face_value, coupon_rate, maturity_years, ytm)
print(
    f"Bond price with {coupon_rate*100}% coupon, {maturity_years}Y maturity, {ytm*100}% YTM: ${bond_px:.2f}"
)
print(f"Macaulay duration: {duration:.2f} years")

# Test loan functions
print("\n--- Loan Functions ---")
principal = 300000
annual_rate = 0.05
loan_years = 30

monthly_payment = qf.tvm.loan_payment(principal, annual_rate, loan_years, 12)
total_interest = qf.tvm.total_interest_paid(principal, annual_rate, loan_years, 12)
print(
    f"Monthly payment on ${principal:,} loan at {annual_rate*100}% for {loan_years} years: ${monthly_payment:,.2f}"
)
print(f"Total interest paid: ${total_interest:,.2f}")

# Test cash flow analysis
print("\n--- Cash Flow Analysis ---")
cash_flows = [-100000, 30000, 40000, 50000]
discount_rate = 0.10

npv = qf.tvm.net_present_value(cash_flows, discount_rate)
irr = qf.tvm.internal_rate_of_return(cash_flows)
payback = qf.tvm.payback_period(cash_flows)

print(f"Cash flows: {cash_flows}")
print(f"NPV at {discount_rate*100}% discount rate: ${npv:,.2f}")
if np.isnan(irr):
    print("IRR: Could not be calculated (no solution found)")
else:
    print(f"IRR: {irr*100:.2f}%")
print(f"Payback period: {payback:.2f} years")

# Test amortization schedule (first few payments)
print("\n--- Amortization Schedule (First 5 payments) ---")
schedule = qf.tvm.amortization_schedule(100000, 0.06, 15, 12)
print(schedule.head().round(2))

print("\n✅ All TVM tests completed successfully!")
