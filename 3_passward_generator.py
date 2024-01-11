import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def okay():
    print("=== Password Generator ===")
    try:
        password_length = int(input("Enter the desired length: "))
        if password_length <= 0:
            print("Invalid password length")
        else:
            generated_password = generate_password(password_length)
            print(f"\nGenerated Password: {generated_password}")
    except ValueError:
        print("Invalid input.")

okay()