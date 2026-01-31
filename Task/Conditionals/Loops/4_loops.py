users = [
    {"name": "Ivanov", "debt": 250, "service": "Internet"},
    {"name": "Petrov", "debt": 0, "service": "TV"},
    {"name": "Sidorov", "debt": 500, "service": "Internet"},
    {"name": "Bondar", "debt": 0, "service": "Internet"},
    {"name": "Kuzmenko", "debt": 120, "service": "TV"}
]


for user in users:
        if user["service"] == "Internet" and user["debt"]>400:
            print(user["name"],"користується",user["service"],"і винен",user["debt"],"грн")
            break
    