print("Welcome to Pizza Deliveries !")
size = input("What size pizza do you want? (s,m,l): ")
add_pepperoni = input("Do you want pepperoni? (y,n): ")
extra_cheese = input("Do you want extra cheese? (y,n): ")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is {bill} INR.")
