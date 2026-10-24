# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    """Represent a record in the unbound-method debugging exercise."""

    def __init__(self, label, value, limit):
        """Store the label, measured value, and limit on this instance."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return whether this record exceeds its limit."""
        return "OVER LIMIT" if self.value > self.limit else "OK"

# Calling status without the object demonstrates the intended NameError.
r = Record("R-001", 120.0, 100.0)
print(r.status())
