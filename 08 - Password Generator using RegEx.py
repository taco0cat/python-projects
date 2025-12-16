import re
import secrets
import string

def generate_password(length = 16, nums = 1, special_chars = 1, uppercase = 1, lowercase = 1):
    
    # Calculate how many specific characters are strictly required
    total_required = nums + special_chars + uppercase + lowercase
    
    # SAFETY GUARD 1: Check for Impossible Constraints
    if total_required > length:
        print(f"Error: Impossible constraints! You asked for {total_required} specific chars, but length is only {length}.")
        return None
    
    # SAFETY GUARD 2: Build a Dynamic Pool
    all_characters = ""
    if lowercase > 0:
        all_characters += string.ascii_lowercase
    if uppercase > 0:
        all_characters += string.ascii_uppercase
    if nums > 0:
        all_characters += string.digits
    if special_chars > 0:
        all_characters += string.punctuation

    if not all_characters:
        print("Error: No character types selected!")
        return None

    # Generate password
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # Define constraints based on user input
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{string.punctuation}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check if password meets the MINIMUM counts
        # Note: We use <= because if you ask for 1 number, getting 2 is fine.
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    # nums = 5 means minimum 5 numbers should appear in the generated password, etc.
    new_password = generate_password(length=16, nums=5, special_chars=1, uppercase=2, lowercase=2)
    print('Generated password:', new_password)