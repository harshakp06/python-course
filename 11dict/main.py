import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detial = response.json()

print(len(complete_detial))

# print(complete_detial[0])

print(complete_detial[0]["user"]["login"])

for i in range(len(complete_detial)):
    print(complete_detial[i]["user"]["login"])


