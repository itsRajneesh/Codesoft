import random
import string
def generate_password(length):
# Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password using random.choices
    password = ''.join(random.choices(characters, k=length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
# Access to user for the desired password length
        length = int(input("Enter the desired password length: "))
# Check if the length is valid
        if length <= 0:
            print("Please enter a valid password length.")
            return
# Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
if __name__ == "__main__":
    main()