# =====================================
# TASK 7 - EMI CALCULATOR
import math
# Function to calculate EMI
def calculate_emi(principal_amount, annual_interest_rate, loan_tenure_years):

    monthly_interest_rate = annual_interest_rate / (12 * 100)

    number_of_months = loan_tenure_years * 12

    emi = (
        principal_amount
        * monthly_interest_rate
        * math.pow(1 + monthly_interest_rate, number_of_months)
    ) / (
        math.pow(1 + monthly_interest_rate, number_of_months) - 1
    )
    return emi
# Taking input from user
principal_amount = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
loan_tenure_years = int(input("Enter loan tenure in years: "))

# Calculating EMI
monthly_emi = calculate_emi(
    principal_amount,
    annual_interest_rate,
    loan_tenure_years
)
# Displaying result
print("\n========== EMI CALCULATOR ==========")

print(f"Loan Amount        : ₹{principal_amount}")
print(f"Interest Rate      : {annual_interest_rate}%")
print(f"Loan Tenure        : {loan_tenure_years} years")
print(f"Monthly EMI        : ₹{monthly_emi:.2f}")



# =====================================
# TAX CALCULATOR

# Function to calculate tax
def calculate_tax(annual_income):
    tax_amount = 0
    if annual_income <= 250000:

        tax_amount = 0
    elif annual_income <= 500000:

        taxable_income = annual_income - 250000

        tax_amount = taxable_income * 0.05
    elif annual_income <= 1000000:
        tax_amount = (
            250000 * 0.05
            + (annual_income - 500000) * 0.20
        )
    else:
        tax_amount = (
            250000 * 0.05
            + 500000 * 0.20
            + (annual_income - 1000000) * 0.30
        )
    return tax_amount
# Taking input
annual_income = float(input("\nEnter annual income: "))
# Calculating tax
income_tax = calculate_tax(annual_income)
# Displaying output
print("\n========== TAX CALCULATOR ==========")

print(f"Annual Income      : ₹{annual_income}")
print(f"Income Tax         : ₹{income_tax:.2f}")