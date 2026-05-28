hash_value = input("enter a hash string: ").lower()
length = len(hash_value)
print("\nHash Length:", length , 'characters')
if length == 32 :
    print("hash type: MD5")
elif length == 40 :
    print("hash type: SHA-1")
elif length == 64 :
    print("hash type:  SHA-256")
elif length == 128 :
    print("hash type: SHA-512")
else:
    print("unknown hash type")
    

