"""
RECORD CHECK  -  my version
===========================

Name  :  Zahraa Ali Mohsin
Lane  :  AI
Date  :  06/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
# This function decides the status using the percentage of the value against the limit.
# If the value reaches 100% or more, it is over the limit. If it is close to the limit,
# it is a warning. Otherwise it is acceptable.
overlimit_count = 0


def status_of(percent):
    global overlimit_count
    if percent >= 100:
        status = "OVER LIMIT"
        overlimit_count += 1
        return status
    elif percent >= 90:
        status = "WARNING"
        return status
    else:
        status = "OK"
        return status


# This function calculates the difference between value and limit,
# then works out the percentage relative to the limit. If the limit is zero,
# the percentage is treated as 0 to avoid division by zero.
def check(value, limit):
    difference = value - limit
    percent = 0 if limit == 0 else (value / limit) * 100
    return difference, percent


# This function prints a neat report showing the label, values, and result status.
def print_report(label, value, limit, difference, percent, status, overlimit_count):
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print("=" * 34)
    print(f"  Value:      {value:>10.2f}")
    print(f"  Limit:      {limit:>10.2f}")
    print(f"  Difference: {difference:>10.2f}")
    print(f"  Percentage: {percent:>10.2f}%")
    print(f"  Status:     {status}")
    print("=" * 34)
    print(f"Over Limit Count: {overlimit_count}")


# ==================================================================== INPUT
# Keep asking for records until the user chooses to quit.
while True:
    label = input("Label (q to quit): ").strip()
    if label.lower() == "q" or label.lower() == "quit":
        print("Exiting the program.")
        print(f"Over Limit Count: {overlimit_count}")
        break

    value = float(input("Enter Value: "))
    limit = float(input("Enter Limit: "))

    # ================================================================== PROCESS
    # Calculate the difference and percentage, then classify the result.
    difference, percent = check(value, limit)
    status = status_of(percent)

    # =================================================================== OUTPUT
    # Print the detailed record check result for this input.
    print_report(label, value, limit, difference, percent, status, overlimit_count)

