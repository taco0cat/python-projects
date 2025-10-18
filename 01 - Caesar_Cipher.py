def caesar(text, shift, encrypt=True):

    # Validating only integers for shift variable
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validating shift between 1 and 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If encrypt is false, shift will be negative
    if not encrypt:
        shift = -shift
    
    # Shifting alphabet based on parameter given
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Creating translation table using str.maketrans(a, b) # A is mapped to B
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    # Encrypting/decrypting text
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# Example
# encrypted_text = encrypt('freeCodeCamp', 3)
# print(encrypted_text)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

# OUTPUT
    # Courage is found in unlikely places.