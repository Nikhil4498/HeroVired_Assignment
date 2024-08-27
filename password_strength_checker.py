#Password Strength Checker

import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for both uppercase and lowercase letters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

# User input
password = input("Enter a password to check its strength: ")

if check_password_strength(password):
    print("Password is strong.")
else:
    print("Password is weak. Please make sure it meets the required criteria.")

