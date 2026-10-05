"""
RECORD CHECK  -  my version
===========================

Name  : Zahraa Ali Mohsin
Lane  :  AI 
Date  : 29/09/2026

Run it:   python template.py

"""


label = input("Enter the label (text): ")
first = float(input("Enter the first value (number): "))
second = float(input("Enter the second value (number): "))

difference = first - second
print(f"Difference: {difference:+.2f}") 

percent = (first / second) * 100
print(f"Percent: {percent:.2f}%") 
 


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print(f"  First:  {first:>10.2f}")
print(f"  Second: {second:>10.2f}")
print(f"  Difference: {difference:>+10.2f}")
print("=" * 34)
print(f" Diff+Percent: {difference + percent:>+10.2f}")
print("=" * 34)
print(f"  Difference: {difference:>+10.2f}")
print(f"  Percent:    {percent:>10.2f}%")
# : your report lines go here
print(f"  Average:    {(first + second) / 2:10.2f}")
print("=" * 34)


