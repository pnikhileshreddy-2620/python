from python.day3.Ticket_Roll_coaster import height



if height>=120 :
    print("can Ride")
    age = int(input("Enter the age :"))
    if age <=18:
        print("You have to pay  $7 ")
    else:
        print("You have to pay $12")
else:
    print("can't ride")