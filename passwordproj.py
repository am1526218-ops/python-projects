import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("password length must be at least 4")
    
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    remaining = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    others = [random.choice(all_chars) for _ in range(remaining)]

    password_list = [lower, upper, digit, symbol] + others
    random.shuffle(password_list)

    return ''.join(password_list)

print(generate_password(12))