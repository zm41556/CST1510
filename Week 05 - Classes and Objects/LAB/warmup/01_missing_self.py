# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    """Represent a record in the missing-self debugging exercise."""

    def status(self, percent):
        """Return a percentage; omitting self is intentional for this exercise."""
        return percent

# This call raises TypeError because a bound method receives the object too.
r = Record()
print(r.status(95))
