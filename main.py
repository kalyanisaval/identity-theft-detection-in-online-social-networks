print("Identity Theft Detection Project")

users = [
    {"name": "User1", "login_attempts": 2},
    {"name": "User2", "login_attempts": 8}
]

for user in users:
    if user["login_attempts"] > 5:
        print(user["name"], "Suspicious Activity")
    else:
        print(user["name"], "Normal Activity")