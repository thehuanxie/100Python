import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text:str, shift:int, direction:str)-> str:
    cipher_text = ""
    if shift > 26:
        shift %= 26
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "decode":
                new_position = position - shift
            elif direction == "encode" and position > shift:
                new_position = position + shift - len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return f"The {direction} text is {cipher_text}"

print(art.logo)

go_ahead = True
while go_ahead:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(text, shift, direction))

    go_ahead = True if input("Do you want to do it again? Yes/No").lower() == "yes" else False

