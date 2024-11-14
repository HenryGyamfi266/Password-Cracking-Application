import hashlib
import itertools
import time

# Target hash to crack is (e.g., hash of "hello" using MD5)
target_hash = "5d41402abc4b2a76b9719d911017c592"  # You can replace with your target hash

# Default character set for brute-force attack
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def hash_password(password, algorithm='md5'):
    """
    Hashes the input password using the specified algorithm and returns the hash.
    """
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    # results for using sha256


# Here I write the brute-force attack function
def brute_force_attack(target_hash, max_length, algorithm='md5'):
    """
    Attempts to crack the password using a brute-force approach by generating all combinations
    of characters up to a specified length and comparing their hashes to the target hash.
    """
    print("Starting brute-force attack...")
    start_time = time.time()
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if hash_password(guess, algorithm) == target_hash:
                end_time = time.time()
                print(f"Password found: {guess}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess
    print("Password not found in the given brute-force range.")
    return None


# Here I build the dictionary attack function
def dictionary_attack(target_hash, dictionary_file, algorithm='md5'):
    """
    Attempts to crack the password by reading each line in a dictionary file as a possible password
    and comparing the hash to the target hash.
    """
    print("Starting dictionary attack...")
    start_time = time.time()
    try:
        with open(dictionary_file, "r") as file:
            for line in file:
                password = line.strip()
                if hash_password(password, algorithm) == target_hash:
                    end_time = time.time()
                    print(f"Password found: {password}")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return password
    except FileNotFoundError:
        print("Dictionary file not found.")
    print("Password not found in the dictionary file.")
    return None


# Here I write the simulated rainbow table function
def rainbow_table_attack(target_hash, precomputed_hashes):
    """
    Simulates a rainbow table attack by using a dictionary of precomputed password-hash pairs
    to find the password matching the target hash.
    """
    print("Starting rainbow table attack...")
    start_time = time.time()
    if target_hash in precomputed_hashes:
        password = precomputed_hashes[target_hash]
        end_time = time.time()
        print(f"Password found: {password}")
        print(f"Time taken: {end_time - start_time} seconds")
        return password
    else:
        print("Password not found in the rainbow table.")
        return None


# Here I write the mask-based brute-force function
def mask_based_brute_force(target_hash, mask, charset, algorithm='md5'):
    """
    Attempts to crack the password by following a pattern (mask) where each '?' represents
    any character in the charset.
    """
    print("Starting mask-based brute-force attack...")
    slots = mask.count('?')
    combinations = itertools.product(charset, repeat=slots)
    start_time = time.time()
    attempts = 0

    for guess_tuple in combinations:
        guess = list(mask)
        guess_idx = 0
        for i, char in enumerate(mask):
            if char == '?':  # Replace only the '?' placeholders
                guess[i] = guess_tuple[guess_idx]
                guess_idx += 1
        guess = ''.join(guess)

        if hash_password(guess, algorithm) == target_hash:
            end_time = time.time()
            print(f"Password found: {guess}")
            print(f"Attempts: {attempts}, Time taken: {end_time - start_time} seconds")
            return guess
        attempts += 1
    print("Password not found within the given mask.")
    return None


# Main function to demonstrate different attack methods
def main():
    # Precomputed hashes for rainbow table (simulated)
    precomputed_hashes = {
        hash_password("password123"): "password123",
        hash_password("123456"): "123456",
        hash_password("admin"): "admin",
        hash_password("letmein"): "letmein",
        hash_password("hello"): "hello"
    }

    # Here I Choose the preferred attack method
    print("Choose an attack method:\n1. Brute-force\n2. Dictionary\n3. Rainbow Table\n4. Mask-based Brute-force")
    choice = input("Enter your choice (1/2/3/4): ")

    # Select hashing algorithm
    algorithm = input("Enter hashing algorithm (md5 or sha256): ").lower()
    if algorithm not in ["md5", "sha256"]:
        print("Invalid algorithm. Defaulting to MD5.")
        algorithm = "md5"

    if choice == "1":
        # Brute-force attack with max length of characters to try
        max_length = int(input("Enter maximum password length for brute-force attack: "))
        brute_force_attack(target_hash, max_length, algorithm)

    elif choice == "2":
        # Dictionary attack with a dictionary file path
        dictionary_file = input("Enter dictionary file path: ")
        dictionary_attack(target_hash, dictionary_file, algorithm)

    elif choice == "3":
        # Rainbow table attack with a precomputed hash table
        rainbow_table_attack(target_hash, precomputed_hashes)

    elif choice == "4":
        # Mask-based brute-force attack
        mask = input("Enter mask pattern (use '?' as placeholder): ")
        mask_based_brute_force(target_hash, mask, charset, algorithm)

    else:
        print("Invalid choice.")


# Run the main function
if __name__ == "__main__":
    main()
