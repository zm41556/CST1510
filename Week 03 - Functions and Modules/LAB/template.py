"""
RECORD CHECK  -  my version
===========================

Name  :  Zahraa Ali Mohsin
Lane  :  AI
Date  :  06/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
"""This function find the status by comparing percentage with 100, 90, and other"""
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

"""This function calculate the diffrence and percent between given value and limit"""
def check(value, limit):
    difference = (value - limit) if limit != 0 else 0
    percent = (difference / limit * 100) if limit != 0 else 0  
    return difference, percent

"""This function prints a detialed report of the given value, limit and
 also the returned status, difference, percent and the overlimit """
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
while True:
    label = input("Label (q to quit): ").strip()
    if label.lower() == "q" or label.lower() == "quit":
        print("Exiting the program.")
        print(f"Over Limit Count: {overlimit_count}")
        break

    value = float(input("Enter Value: "))
    limit = float(input("Enter Limit: ")) 
    


 # ================================================================== PROCESS
    difference, percent = check(value, limit)      
    status = status_of(percent)  

 # =================================================================== OUTPUT
    print_report(label, value, limit, difference, percent, status, overlimit_count)

