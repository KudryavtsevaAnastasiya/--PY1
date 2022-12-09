def get_random_password() -> str:

    import random
    import string
    length = 8
    symbols = (string.ascii_uppercase, string.ascii_lowercase, string.digits)
    all_symbols = ''.join(symbols)

    return random.sample(all_symbols, length)


password = get_random_password()

print(''.join(password))
# Последняя строка