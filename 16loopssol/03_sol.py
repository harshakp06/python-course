number = int(input("enter the number for table "))

for i in range(1,11):
    if i == 5 :
        continue
    print(f"{number} x {i} = ",number*i)