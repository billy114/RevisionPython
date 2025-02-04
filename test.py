import requests

users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
for user in users:
    print("name : ", user["name"])

