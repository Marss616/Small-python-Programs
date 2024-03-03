# this program will encrypt a message using the Caesar cipher method and a shift key that is generated from the current time

import datetime

def create_shift_key_with_date():
    date = datetime.datetime.now()
    date_split = str(date).split(" ")
    shift = 0  
    
    for i, v in enumerate(date_split):
        if i == 1: 
            for x in v:
                if x.isdigit():
                    shift += int(x)
    return shift % 26

def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) + shift - start) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

text = "Hello, World!"
shift = create_shift_key_with_date()
encrypted_text = caesar_cipher(text, shift)
print(shift)
print(encrypted_text)
