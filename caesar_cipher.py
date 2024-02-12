def encrypt(string, shift):
    cipher = ''
    for char in string: # starting for loop
        if char == ' ':
            cipher += ' '  # Add a space to cipher when char is a space
        elif char == ".": # each symbol "." will turn into "X"
            cipher += "X"  # Add "X" to cipher when char is "."
        elif char.isupper():
            cipher += chr((ord(char) + shift - 65) % 26 + 65) # Encrypt uppercase characters
        else:
            cipher += char  # Add the original character to cipher for all other cases
    return cipher


input_0 = input("Type 'decrypt' to decrypt and 'encrypt' to encrypt only uppercase and symbols allowed *case senstive*")

if input_0 == "encrypt":
    text_0 = input("enter string: ")
    s_0 = 3
    print("after encryption: ", encrypt(text_0, s_0))
elif input_0 == "decrypt":
    text_1 = input("enter string: ")
    s_1 = -3
    s_1 = s_1 if s_1 > 0 else s_1 + 26  # Adjust for negative shift
    print("after decryption: ", encrypt(text_1, s_1))
else:
    print("Invalid input")
