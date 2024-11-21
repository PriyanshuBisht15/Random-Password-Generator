# Random-Password-Generator
This Python program generates random passwords based on user-defined criteria, such as password length and the inclusion of specific character types (uppercase, lowercase, digits, and special characters). It provides a simple interface for generating secure passwords.

## Features:
1. Allows the user to select the length of the password.

2. User can specify if they want uppercase, lowercase, digits, and special characters.

3. Option to generate multiple passwords at once.

## How It Works
1.User Interaction:The program starts by asking the user for inputs:
- Number of password
- Length of each password.
- Preferences for character types.

2.Password Generation: Based on these inputs, passwords are generated using random selections from the character pool.

3.Display:Each generated password is displayed on the screen.

## Usage
## Prerequisites
- Python 3.x

## Running the Program
- Save the script to a file, e.g., password_generator.py.
- Open a terminal or command prompt.
- Run the script using Python:
  python password_generator.py

## Input Prompts
The program will ask for the following inputs:
1. Number of Passwords: Enter how many passwords you want to generate (e.g., 5).

2. Password Length: Specify the length of each password (e.g., 12).

3. Include Uppercase Letters: Type y for yes or n for no.

4. Include Lowercase Letters: Type y for yes or n for no.

5. Include Digits: Type y for yes or n for no.

6. Include Special Characters: Type y for yes or n for no.

## Example Run:

Random Password Generator
How many passwords would you like to generate? 3
Enter the desired password length: 10
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): n

Password 1: X7vRmTqHp4
Password 2: J9kPyWmLz3
Password 3: B4nTsXqHp8

##Code Details
- generate_password(length, use_upper, use_lower, use_digits, use_special)
A helper function that generates a password of the specified length using the chosen character sets.

- main()
The main function that handles user interaction and manages password generation.



