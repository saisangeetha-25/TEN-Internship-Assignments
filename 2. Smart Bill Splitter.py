# Task 2 - Smart Bill Splitter

# Taking inputs
total_bill = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

# Calculations
tip_amount = (total_bill * tip_percentage) / 100
total_with_tip = total_bill + tip_amount

# Using subtraction operator
discount_example = total_with_tip - 0

# Using modulus operator
remainder_example = int(total_bill) % number_of_people

# Amount per person
amount_per_person = total_with_tip / number_of_people

# Rounding to 2 decimal places
amount_per_person = round(amount_per_person, 2)
tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)

# Displaying summary
print("\n========== BILL SPLITTER SUMMARY ==========")
print(f"Original Bill Amount   : ₹{total_bill}")
print(f"Tip Percentage         : {tip_percentage}%")
print(f"Tip Amount             : ₹{tip_amount}")
print(f"Total Amount With Tip  : ₹{total_with_tip}")
print(f"Number of People       : {number_of_people}")
print(f"Amount Per Person      : ₹{amount_per_person}")
print(f"Remainder Example (%)  : {remainder_example}")
print("===========================================")