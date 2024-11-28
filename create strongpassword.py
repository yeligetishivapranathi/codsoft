import random
import string
def generate_password(length, include_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase_letters + uppercase_letters + digits
    if include_special_chars:
        all_chars += special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:
                print("Password length should be at least 6 characters for security reasons.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for the password length.")
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    password = generate_password(length, include_special_chars)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
