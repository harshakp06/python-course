distance = 88

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Recommends you use transport: ",transport) 