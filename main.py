import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """Generates a random password based on user preferences."""
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected!")
        return None

    return ''.join(random.choice(characters) for _ in range(length))


def main():
    print("Random Password Generator")

    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    for i in range(num_passwords):
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        if password:
            print(f"Password {i + 1}: {password}")


if __name__ == "__main__":
    main()
