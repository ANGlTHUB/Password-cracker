import itertools
def password_cracker(password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    attempt = 0
    for length in range(1, 9):
        for guess in itertools.product(characters, repeat=length):
            attempt += 1
            guess = ''.join(guess)
            if guess == password:
                return guess, attempt
    return None, attempt


if __name__ == "__main__":
    target_password = input("Enter the target password: ")
    cracked_password, attempt = password_cracker(target_password)
    if cracked_password:
        print("Password cracked:", cracked_password, "in", attempt, "attempts")
    else:
        print("Password not cracked.")


