import sys
import random
import string

def generate_password(length=12):
    # Combine lowercase letters, uppercase letters, digits, and punctuation symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters based on the requested length
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Default length is 12, but allow user to pass a custom length
    length = 12
    
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
            if length < 4:
                print("Error: Password length should be at least 4 characters.")
                return
        except ValueError:
            print("Error: Please provide a valid number for the password length.")
            print("Usage: python gen.py [length]")
            return

    password = generate_password(length)
    print(f"\nGenerated Password ({length} chars): {password}\n")

if __name__ == "__main__":
    main()
