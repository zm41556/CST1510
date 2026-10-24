"""
DEFINING METHODS
================
A function that lives inside a class, and already knows its own data.
Run:  python 01_defining_methods.py
"""

# --- 1. A method is a function defined inside a class -----------------------
# self gives it access to that object's own attributes - no need to pass
# value and limit in again, the object already has them.

class Record:
    """Represent a record whose summary is provided by an instance method."""

    def __init__(self, label, value, limit):
        """Store the record fields on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        """Return the label, value, and limit as a short string."""
        return f"{self.label}: {self.value}/{self.limit}"


r = Record("R-001", 87.0, 100.0)
print(r.summary())        # R-001: 87.0/100.0 - no arguments needed at the call site


# --- 2. Compare to a Week 3 function doing the same job ----------------------

def summary_function(label, value, limit):
    """Return a record summary using explicitly supplied values."""
    return f"{label}: {value}/{limit}"

print(summary_function("R-001", 87.0, 100.0))   # same result, but you must
                                                    # pass everything, every time


# --- 3. A method can return a calculated value, just like any function -------

class Record2:
    """Represent a record with a method that calculates its percentage."""

    def __init__(self, label, value, limit):
        """Store the record fields on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the value as a percentage of the limit."""
        return (self.value / self.limit) * 100

r2 = Record2("R-002", 120.0, 100.0)
print(r2.percent())     # 120.0


# --- 4. One method can call another, both through self ----------------------

class Record3:
    """Represent a record whose status is derived from its percentage."""

    def __init__(self, label, value, limit):
        """Store the record fields on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the value as a percentage of the limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return the appropriate status for this record's percentage."""
        p = self.percent()      # calling another method on the same object
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

r3 = Record3("R-003", 95.0, 100.0)
print(r3.status())     # WARNING


# --- 5. Same idea, three fields ---------------------------------------------

class Dataset:                                        # AI / Data Science
    """Describe a dataset and the number of rows it contains."""

    def __init__(self, name, rows):
        """Store the dataset name and row count."""
        self.name = name
        self.rows = rows

    def summary(self):
        """Return the dataset name and row count."""
        return f"{self.name}: {self.rows} rows"

class Alert:                                          # Cyber Security
    """Describe an alert whose severity can be escalated."""

    def __init__(self, ip, severity):
        """Store the source address and initial severity."""
        self.ip = ip
        self.severity = severity

    def escalate(self):
        """Raise the alert severity to critical and describe the change."""
        self.severity = "critical"
        return f"{self.ip} escalated to {self.severity}"

class Server:                                         # IT
    """Describe a server and its storage usage."""

    def __init__(self, hostname, used, total):
        """Store the hostname and storage capacity values."""
        self.hostname = hostname
        self.used = used
        self.total = total

    def check_disk(self):
        """Return the used storage as a percentage of total capacity."""
        return (self.used / self.total) * 100

print(Dataset("survey_2026", 1200).summary())
print(Alert("10.0.0.5", "low").escalate())
print(Server("srv-01", 87, 120).check_disk())


# --- TRY IT ------------------------------------------------------------------
# 1. Add a method difference(self) to Record3 that returns self.value - self.limit.
# 2. Write a method summary(self) for Record3 that uses self.status() inside it,
#    returning something like "R-003: WARNING".
