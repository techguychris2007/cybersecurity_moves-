username = input("Enter your username:")
length =len(username)
has_space = ' ' in username
if has_space:
    print("invalid username: username cannot contain spaces")
elif length < 5 :
    print("invalid username: username is too short(min 5 characters required)")
elif length > 15 :
    print("invalid username: username is too long (max 15 characters) ")
else :
    print("valid username")
    print("username in uppercase:", username.upper())
    