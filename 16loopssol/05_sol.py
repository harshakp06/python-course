input_str = str(input("enter the string : ")).lower()

# print(input_str)

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break