import requests

users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
# for user in users:
#     print("name : ", user["name"])

# for user in users:
#     print(user["name"], " habite à ", user["address"]["city"] )

id = input("Donnez l'id : ")
user = requests.get("https://jsonplaceholder.typicode.com/users/"+id).json()
print(user["name"], " habite à ", user["address"]["city"] )


