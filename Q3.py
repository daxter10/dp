import hashlib


def hash_password(password):
    """
    Hash a password using SHA-256 and return its hexadecimal representation.

    Parameters:
        password (str): The password string to be hashed.

    Returns:
        str: The SHA-256 hashed password as a hexadecimal string.
    """
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the password
    sha256_hash.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password


def main():
    # Prompt the user for a password
    password = input("Enter the password to hash: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Print the hashed password
    print(f"SHA-256 Hashed Password: {hashed_password}")


if __name__ == "__main__":
    main()
