import itertools
import string

CORRECT_PASSWORD = "abcde"
DICTIONARY_WORDS = ["password", "12345", "qwerty", "abcde", "letmein", "welcome"]

def dictionary_attack():
    print("Starting Dictionary Attack...")
    for word in DICTIONARY_WORDS:
        print(f"Trying: {word}")
        if word == CORRECT_PASSWORD:
            print(f"Dictionary Attack Successful! Password: {word}")
            return True
    print("Dictionary Attack Failed!")
    return False

def brute_force_attack():
    print("Starting Brute Force Attack...")
    chars = string.ascii_letters  
    for attempt in itertools.product(chars, repeat=5):
        attempt_password = "".join(attempt)
        print(f"Trying: {attempt_password}")
        if attempt_password == CORRECT_PASSWORD:
            print(f"Brute Force Attack Successful! Password: {attempt_password}")
            return

if not dictionary_attack():
    brute_force_attack()