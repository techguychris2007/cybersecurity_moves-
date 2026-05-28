import math
password = input("Enter your password: ")
password_length = len(password)
pool = 0
has_lower = any(c in "abcdefghijklmnopqrstuvwxyz" for c in password)
has_upper = any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password)
has_digits = any(c in "0123456789" for c in password)
has_symbols = any(c in "!@#$%^&*()-+" for c in password)

if has_lower: pool +=26
if has_upper: pool +=26
if has_digits: pool +=10
if has_symbols: pool +=33
if pool > 0:
    entropy = password_length * math.log2(pool)
    entropy = round(entropy, 2)
    print(f"password entropy: {entropy} bits")
if entropy < 40 :
    print("Rating: Weak password")
elif entropy < 60 :
    print("Rating: Moderate password")
else:
    print("Rating: Strong password")


