import requests

# users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
# for user in users:
#     print("name : ", user["name"])

# for user in users:
#     print(user["name"], " habite à ", user["address"]["city"] )

# id = input("Donnez l'id : ")
# user = requests.get("https://jsonplaceholder.typicode.com/users/"+id).json()
# print(user["name"], " habite à ", user["address"]["city"] )

# username = input("Donnez le username : ")
# for user in users:
#     if user["username"] == username:
#         print(user["name"], " habite à ", user["address"]["city"] )

# post_id = input("Donnez l'id du post : ")
# post = requests.get("https://jsonplaceholder.typicode.com/posts/"+post_id).json()
# user_id = str(post["userId"])
# user = requests.get("https://jsonplaceholder.typicode.com/users/"+user_id).json()
# print(user["name"], "est celui qui a publié le post ", post_id)

user_id = input("Donnez le userID: ")
n = 0
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
for post in posts:
    if post["userId"] == int(user_id):
        n += 1

user = requests.get("https://jsonplaceholder.typicode.com/users/"+user_id).json()
print(user["name"], "a publié ", n, " posts")