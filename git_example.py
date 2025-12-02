import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    pwd = generate_password(16)
    print(f"Generated password: {pwd}")

    Neew lines