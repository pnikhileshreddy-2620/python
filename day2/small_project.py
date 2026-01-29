"""
Tip calculator system
"""
from typing import final

print("Welcome to tips system")
total_bill = float(input("Enter the total bills :"))
tips = float(input("How much tip would like to give ? 10,12, or 15 "))
number_people = int(input("How many people the split  the bills "))

Bill_after_tips = total_bill*(tips/100)
print("Total Amount :",total_bill+Bill_after_tips)
print("Per person to pay the bill :",(total_bill+Bill_after_tips)/number_people)