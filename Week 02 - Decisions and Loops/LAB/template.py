"""
RECORD CHECK  -  my version
===========================

Name  :  Zahraa Ali Mohsin
Lane  :  AI 
Date  :  01/10/2026

Run it:   python template.py

"""
overlimit_count = 0
while True:
    label = input("Label (q to quit): ").strip().lower()
    if label == "q" or label == "quit":
        print("Exiting the program.")
        print(f"Over Limit Count: {overlimit_count}")
        break

    value = float(input("Value: "))    
    limit = float(input("Limit: "))    

    difference = value - limit   
    percent = (difference / limit * 100) if limit != 0 else 0      

    if percent >= 100:
        status = "OVER LIMIT"
        overlimit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    #report lines go here
    print("=" * 34)
    print(f"  Value:      {value:>10.2f}")
    print(f"  Limit:      {limit:>10.2f}")
    print(f"  Difference: {difference:>10.2f}")
    print(f"  Status:     {status}")
    print("=" * 34)
    print(f"Difference: {difference:>10.2f}")
    print(f"Percentage: {percent:>10.2f}%")
    print("=" * 34)
    print(f"Over Limit Count: {overlimit_count}")

