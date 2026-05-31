# =====================================
# TASK 8- ATTENDANCE CALCULATOR
# =====================================

# Function to calculate attendance percentage
def calculate_attendance(attended_classes, total_classes):

    attendance_percentage = (
        attended_classes / total_classes
    ) * 100

    return attendance_percentage


# Taking input from user
total_classes = int(input("Enter total classes conducted: "))

attended_classes = int(input("Enter attended classes: "))

required_percentage = float(input("Enter required attendance percentage: "))

# Calculating attendance
attendance_percentage = calculate_attendance(
    attended_classes,
    total_classes
)
# Displaying attendance
print("\n========== ATTENDANCE REPORT ==========")

print(f"Total Classes          : {total_classes}")
print(f"Classes Attended       : {attended_classes}")
print(f"Attendance Percentage  : {attendance_percentage:.2f}%")

# Checking eligibility
if attendance_percentage >= required_percentage:
    print("Attendance requirement met ✅")
else:
    print("Attendance requirement not met ❌")

    # Calculating extra classes needed
    extra_classes = 0
    while (
        (attended_classes + extra_classes)
        / (total_classes + extra_classes)
    ) * 100 < required_percentage:
        extra_classes += 1
    print(
        f"Attend at least {extra_classes} more classes "
        f"to reach {required_percentage}% attendance."
    )