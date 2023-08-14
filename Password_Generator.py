import random

def generate_secret_key(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    secret_key = ""
    for _ in range(length):
        random_character = random.choice(characters)
        secret_key += random_character
    return secret_key

print("""Welcome to the Secret Key Generator!Here you get a Strong Password,
        Strong passwords bolster cybersecurity,thwarting unauthorized access and data breaches.""")

print('                            ')
length = int(input("Specify the length of the desired secret key: "))

if length <= 0:
    print("Oops! Please enter a positive number.")
else:
    secret_key = generate_secret_key(length)
    print("Your Generated Secret Key:", secret_key)
