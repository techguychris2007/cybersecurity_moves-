correct_password = "chrisB1234"
correct_username = "chris"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("login successful")
    print("welcome", username)
elif username != correct_username and password == correct_password:
    print("invalid username. Access denied")
else:
    print("invalid username or password. Access denied")