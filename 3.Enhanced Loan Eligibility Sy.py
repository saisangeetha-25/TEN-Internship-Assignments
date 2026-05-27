# TASK 03 - Enhanced Loan Eligibility System

# Taking user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
employment_type = input("Enter employment type (salaried/self-employed): ").lower()

print("\n========== LOAN ELIGIBILITY RESULT ==========")

# Checking eligibility conditions
if age < 21:
    print("Rejected: Applicant must be at least 21 years old.")

elif age > 60:
    print("Rejected: Applicant age exceeds maximum limit of 60.")

elif salary < 25000:
    print("Rejected: Minimum salary requirement is ₹25,000.")

elif employment_type not in ["salaried", "self-employed"]:
    print("Rejected: Invalid employment type.")

elif age >= 21 and age <= 30 and salary < 30000:
    print("Needs Guarantor: Young applicant with lower salary.")

elif age > 55 and employment_type == "self-employed":
    print("High Risk: Senior review needed for self-employed applicant.")

else:
    print("Loan Approved ✅")

print("=============================================")