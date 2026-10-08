
# This function compares a value with a limit and returns the result.
def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

# Call the function and store the result in a variable.
status = check(87, 100)

# Print the result for the user.
print(status)
