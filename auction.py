import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
bid={}
cont=True
print("welcome to auction, please type your name first and then pass on to the next ones for continue the bid")
input("Enter what you want to bid on: ")
while cont:
    name=input("Enter your name: ")
    amt=int(input("Enter the bid amount: $"))
    bid[name]=amt
    k=input("still people are there to bid around you then type 'yes' else type 'no'").lower()
    if k=='no':
        cont=False
    clear_screen()
highest_key=max(bid)
print(bid)
print("the highest bidder is ",highest_key," and amount is $",bid[highest_key])