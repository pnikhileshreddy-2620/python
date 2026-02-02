"""
Bid game using dictionary

"""


bid={}
i =True
while i:
    uname = input("Enter the name :")
    price =float(input("enter your bid :"))
    bid[uname]=price
    exit=input("Are there any bidder Type yes or NO ").upper()
    print('\n'*50)
    if exit=='NO':
        i=False
print(bid)
print(f"The winner is {max(bid,key=bid.get)} and bid is {max(bid.values())}")