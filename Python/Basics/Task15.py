import ceasar_cipher_art as cs
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(f"{cs.logo}")
end = True

def ceasar(some_text, shift_amount, going_direction):
    plain_text = ""
    if going_direction == "decode":
        shift_amount *=-1
    for char in some_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The {going_direction}d text is {plain_text}")

while end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(some_text=text, shift_amount=shift, going_direction=direction)
    answer = input("Would you like to restart? ").lower()
    if answer == "no":
        end = False
        print("Goodbye! Have a nice day ahead.")
