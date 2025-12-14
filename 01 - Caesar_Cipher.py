import string

alphabet = string.ascii_letters + string.digits + string.punctuation + ' '

def caesar(text, shift, encrypt=True):

    # Validating only integers for shift variable
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validating shift between 1 and 25
    if shift < 1:
        return 'Shift must be greater than 0.'
    if shift > len(alphabet):
        shift = shift % len(alphabet)

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
encrypt_text = encrypt('freeCodeCamp', 3)
print(encrypt_text)

encrypt_text2 = encrypt("Courage is found in unlikely places.", 13)
print(encrypt_text2)

encrypted_text3 = "PBHEntrMvFMsBHAqMvAMHAyvxryLMCynprF_"
decrypted_text = decrypt(encrypt_text2, 13)
print(decrypted_text)