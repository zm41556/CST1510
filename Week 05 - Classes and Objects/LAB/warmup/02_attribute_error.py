# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    """Represent a record in the attribute-name debugging exercise."""

    def __init__(self, label, value, limit):
        """Store the supplied fields, using amount instead of value on purpose."""
        self.label = label
        self.value = value   # The exercise expects the attribute to be named value.
        self.limit = limit

# Accessing value demonstrates that the intended attribute was not set.
r = Record("R-001", 87.0, 100.0)
print(r.value)
