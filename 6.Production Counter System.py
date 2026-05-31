# =====================================
# TASK 2 - PRODUCTION COUNTER SYSTEM
# =====================================

import random

# Taking input from user
target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate percentage: "))

# Variables
total_units_produced = 0

print("\n========== PRODUCTION REPORT ==========")

# Simulating 3 shifts
for shift in range(1, 4):

    shift_production = 0
    defect_count = 0

    print(f"\n----- SHIFT {shift} STARTED -----")

    # Simulating 20 machine cycles
    for cycle in range(1, 21):

        # Stop production if target reached
        if total_units_produced >= target_units:
            print("\nTarget achieved. Production stopped.")
            break

        # Random defect generation
        random_number = random.randint(1, 100)

        if random_number <= defect_rate:

            defect_count += 1

            print(f"Cycle {cycle}: Defective item skipped")

            continue

        # Successful production
        shift_production += 1
        total_units_produced += 1

        print(f"Cycle {cycle}: Item produced successfully")

    # Worker productivity
    worker_productivity = round(
        shift_production / workers_per_shift, 2
    )

    # Shift report
    print("\nShift Summary")
    print("Items Produced :", shift_production)
    print("Defects Found  :", defect_count)
    print("Worker Productivity :", worker_productivity)

    # Stop outer loop also
    if total_units_produced >= target_units:
        break

# Final report
print("\n========== FINAL REPORT ==========")
print("Total Units Produced :", total_units_produced)
print("Production Completed Successfully")