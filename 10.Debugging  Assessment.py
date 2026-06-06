# =====================================
# BUG 1 - RUNTIME ERROR
# =====================================

# Type : IndexError

# Cause :
# Trying to access a list position that does not exist.

# Fix :
# Access only valid indexes inside the list.

# BUGGY CODE:

# marks = [80, 90, 70, 85, 95]
# print(marks[10])

# FIXED CODE:

# marks = [80, 90, 70, 85, 95]
# print(marks[4])


# =====================================
# BUG 2 - LOGICAL ERROR
# =====================================

# Type : Logical Error

# Cause :
# Average calculated using wrong divisor.

# Fix :
# Divide total by number of students.

# BUGGY CODE:

# marks = [80, 90, 70, 85, 95]
# total = sum(marks)
# average = total / 4
# print(average)

# FIXED CODE:

# marks = [80, 90, 70, 85, 95]
# total = sum(marks)
# average = total / 5
# print(average)


# =====================================
# FINAL MARKS CALCULATOR PROGRAM
# =====================================

marks = []

for i in range(5):

    mark = float(
        input(f"Enter marks of student {i + 1}: ")
    )

    marks.append(mark)

total_marks = sum(marks)

average_marks = total_marks / len(marks)

highest_marks = max(marks)

lowest_marks = min(marks)

print("\n===== MARKS REPORT =====")

print("Total Marks   :", total_marks)

print("Average Marks :", average_marks)

print("Highest Marks :", highest_marks)

print("Lowest Marks  :", lowest_marks)