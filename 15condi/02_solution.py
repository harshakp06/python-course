age = int(input("enter age "))
# age = 18

day = "Wednesday"

price = 12 if age > 17 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price is $",price)