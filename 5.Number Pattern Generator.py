# =====================================
# TASK 5 - NUMBER PATTERN GENERATOR
# =====================================

# Taking input from user
n = int(input("Enter a number: "))

# -------------------------------------
# 1. Right Triangle of Stars
# -------------------------------------

print("\n1. Right Triangle of Stars")

for row in range(1, n + 1):

    for column in range(row):
        print("*", end=" ")

    print()


# -------------------------------------
# 2. Inverted Triangle of Numbers
# -------------------------------------

print("\n2. Inverted Triangle of Numbers")

for row in range(n, 0, -1):

    for column in range(1, row + 1):
        print(column, end=" ")

    print()


# -------------------------------------
# 3. Pascal's Triangle
# -------------------------------------

print("\n3. Pascal's Triangle")

for row in range(n):

    value = 1

    for space in range(n - row - 1):
        print(" ", end="")

    for column in range(row + 1):

        print(value, end=" ")

        value = value * (row - column) // (column + 1)

    print()


# -------------------------------------
# 4. Prime Numbers up to n
# -------------------------------------

print("\n4. Prime Numbers up to", n)

for number in range(2, n + 1):

    for divisor in range(2, number):

        if number % divisor == 0:
            break

    else:
        print(number, end=" ")