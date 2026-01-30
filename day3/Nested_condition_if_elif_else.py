from python.day3.Ticket_Roll_coaster import height
bill=0
if height>=120:
    age = int(input("Enter the age :"))
    if age <12:
        bill=8
        print(f"You have to pay ${bill} ")
    elif    12<age<18:
        bill=7
        print(f"You have to pay ${bill}")
    else:
        bill=12
        print(f"You have to pay ${bill}")
photo = input("Do you want to photo yes/No ").lower()
if photo=='yes':
    bill =bill+3
    print("Total " ,bill)


else:
    print("You  can't ride")