
# This function checks the status based on the percentage.
# It uses a default warning threshold of 90 if no value is given.
def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

# Calling the function with one value uses the default threshold.
print(status_of(95))
