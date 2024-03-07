# for i in range(10):
#     print(i)

# Function to check if a string is a palindrome using an iterative approach
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# Test the function with an example string
s = "malayalams"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
