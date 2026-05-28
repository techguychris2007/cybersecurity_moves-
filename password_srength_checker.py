password = input("Enter your  password:")
length = len(password)
print("password length:" , length)
if length < 8 :
    print("password is too short")
elif length > 8 and length < 11 :
    print("moderate password, consider making it longer")
else: 
    print("strong password")
has_digit = ('0' in password or '1' in password or '2' in password)
print('Contains digit:', has_digit)

password = "chris2020"
