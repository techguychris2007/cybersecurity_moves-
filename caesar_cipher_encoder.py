message = input("Enter a message to encrypt: ")
shift = int(input('Enter the shift value (1-25): '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_message = ''
message = message.lower()
print("original message:", message )
print("shift value:" , shift)

print('Note: full loop-based cipher requires loops (coming in the next module)')
print("Demonstrating single character shift:")
first_char =message[0]
if first_char in alphabet:
    idx = alphabet.find(first_char)
    new_idx = (idx + shift) % 26
    encrypted_message += alphabet[new_idx]

print('First character', first_char, '->', alphabet[new_idx])