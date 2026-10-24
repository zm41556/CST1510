"""Record Check — Week 05 mini-project.

Name: Zahraa Ali Mohsin
Lane: AI / Data Science
Date: 24/10/2026

Run this file from the LAB folder with ``python template.py``.
"""

# ====================================================================== CLASS

class Record:
    """Store one labeled value and the limit used to assess it."""

    def __init__(self, label, value, limit):
        """Initialize a record with its label, measured value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value as a percentage of its limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        if percent >= 90:
            return "WARNING"
        return "OK"

# ==================================================================== RECORDS

def load_records(path):
    """Load comma-separated label, value, and limit rows as Record objects."""
    records = []
    with open(path, "r", encoding="utf-8") as records_file:
        for line in records_file:
            if not line.strip():
                continue
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("records_sample.txt")

# ==================================================================== OUTPUT

over_limit_count = 0
for record in records:
    # Store the result once so reporting and counting use the same status.
    status = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print(f"  Label: {record.label}: Value: {record.value} Limit: {record.limit}")
    print(f"  Record Status: {status}")
    print("=" * 34)
    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} of {len(records)} were over limit")
print()


# ==========================================================================

