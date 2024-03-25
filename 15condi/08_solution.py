pas = "jksmnaksddxaadsk"

if len(pas) < 6:
    strength = "weak"
elif len(pas) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("password strength is: ",strength)