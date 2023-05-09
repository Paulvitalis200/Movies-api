import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 3, "name": "Joe", "views": 100},
#     {"likes": 10, "name": "How to make REST", "views": 3000},
#     {"likes": 2, "name": "Jeff", "views": 500},
#     {"likes": 1, "name": "Paul", "views": 2999}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + "video/6")

response = requests.patch(BASE + "video/2", {"views": 99, "likes": 101})
print(response.json())
