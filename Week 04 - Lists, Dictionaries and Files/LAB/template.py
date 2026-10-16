"""
RECORD CHECK  -  my version
===========================

Name  :  Zahraa Ali Mohsin
Lane  :  AI
Date  :  14/10/2026

Run it:   python template.py

"""
from pathlib import Path

# =================================================================== FUNCTIONS

overlimit_count = 0  # Count records at or above the limit.


def status_of(percent):
    """
    Decide status from the percentage of the limit.
    At least 100% is over the limit; 90% or more is a warning.
    """
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """
    Return the difference and percentage relative to the limit.
    A zero limit is treated as 0% to avoid division by zero.
    """
    difference = value - limit
    # Avoid dividing by zero when the limit is zero.
    percent = 0 if limit == 0 else (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the record values and status in a bordered report."""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value:      {value:>10.2f}")
    print(f"  Limit:      {limit:>10.2f}")
    print(f"  Difference: {difference:>10.2f}")
    print(f"  Percentage: {percent:>10.2f}%")
    print(f"  Status:     {status}")
    print("=" * 34)


# ====================================================================== STORE


def load_records(path):
    """Read records from a file and return them as a list of dictionaries."""
    try:
        with open(path, "r") as file:
            records = []
            for line in file:
                # Split the row into its three fields.
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
        return records

    except FileNotFoundError:
        print(f"{path} was not found.")
        return []


# Find the data file beside this script.
records_path = Path(__file__).with_name("records_sample.txt")
records = load_records(records_path)
for record in records:
    print(
        f"Label: {record['label']}, Value: {record['value']}, "
        f"Limit: {record['limit']}\n"
    )


def store_records(path, records):
    """Write the records to a file."""
    with open(path, "w") as file:  # "w" creates or replaces the output file.
        for record in records:
            line = f"{record['label']},{record['value']},{record['limit']}\n"
            file.write(line)


# ====================================================== PROCESS + OUTPUT

for record in records:
    difference, percent = check(record["value"], record["limit"])
    status = status_of(percent)
    if status == "OVER LIMIT":
        overlimit_count += 1  # Count records at or above their limit.
    print_report(
        record["label"], record["value"], record["limit"],
        difference, percent, status,
    )
print(f"Over Limit Count: {overlimit_count}")

output_path = Path(__file__).with_name("new_file.txt")
store_records(output_path, records)
