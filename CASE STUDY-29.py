password = input("Enter a sample password: ")
errors = []
if len(password) < 8:
    errors.append("At least 8 characters are required.")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%&*"

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch in special_chars:
        has_special = True

if not has_upper:
    errors.append("Include at least one uppercase letter.")
if not has_lower:
    errors.append("Include at least one lowercase letter.")
if not has_digit:
    errors.append("Include at least one digit.")
if not has_special:
    errors.append("Include at least one special character from !@#$%&*.")
if "password" in password.lower():
    errors.append("Do not include the word 'password'.")

if errors:
    print("Password is INVALID:")
    for error in errors:
        print("-", error)
else:
    print("Password is VALID.")
