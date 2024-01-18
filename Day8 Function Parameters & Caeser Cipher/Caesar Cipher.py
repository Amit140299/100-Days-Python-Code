from operator import index

from matplotlib.patches import CirclePolygon


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction in ('encode','decode'):
    text=input("Type your massage:\n").lower()
    shift=int(input("Type the shift number:\n"))
else:
    print("Gand ke andhe sahi input de!")
    
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        if new_position<=25:
            new_letter=alphabet[new_position] 
            cipher_text+=new_letter
        else:
            new_position=new_position-25-1
            new_letter=alphabet[new_position] 
            cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
    return cipher_text

def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        if new_position>=0:
            new_letter=alphabet[new_position] 
            plain_text+=new_letter
        else:
            new_position=25+new_position+1
            new_letter=alphabet[new_position] 
            plain_text+=new_letter
    print(f"The decoded text is {plain_text}")

# print(alphabet.index('m'))
if direction=='encode':
    encrypt(plain_text=text,shift_amount=shift)
elif direction=='decode':
    decrypt(cipher_text=text,shift_amount=shift)
