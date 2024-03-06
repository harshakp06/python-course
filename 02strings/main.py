arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split("/"))

str1 = "Hello"
str2 = "World"

result = str1+" "+str2
print(result)

#text = "I lead the division that plans and executes the production of made-to-fit clothing for men, by tailoring unit aggregation to fabric and other vendor partners. Skills: Operations Management · Vendor Management · Sales · Marketing · Supply chain"
text = """
I hope this email finds you in good health.I would like to extend our sincerest apologies for the inconvenience caused regarding your recent order with us.
We have reviewed the details of your order and acknowledge that initially, the products were sent out to the wrong address by mistake and sorry to hear that you did not receive any communication from our end for over a month.
Our customer service team will be reaching out to you shortly,we had escalated this issue to the Logistics Partner, we will assure that your order will be delivered on a priority basis.
"""
length = len(text)

text55 = "I would like to extend our apologies for your order, we had esclated this isuue to logistics partner"

print("length of text55: ",len(text55))

print("Length of the string:",length)

# string - upper & lower case
text1 = "python is awesome"
uppercase = text1.upper()
lowercase = text1.lower()
print("Uppercase: ",uppercase)
print("lowercase: ",lowercase)

#  replace text using string replace
new_text1 = text1.replace("awesome","great")
print("Modified text: ",new_text1)

# string split 
text2 = "python is awesome"
words = text2.split()
print("Words:",words)

# string-strip
text3  = "     Some spaces around     "
stripped_text = text3.strip()
print("Stripped text: ",stripped_text)

text4 = "python is awesome"
substring = "is"
if substring in text4:
    print(substring,"found in the text")

# integer variables
num1 = 10
num2 = 5

# integer division
result1 = num1//num2
print("Interger division: ",result1)

# Modulus (Remainder)
result2 = num1 % num2
print("modulus remainder : ",result2)

# Absoluete value
result3 = abs(-7)
print("absolute value : ",result3)

# 