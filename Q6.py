import itertools
import string

def brute_force_attack(target_password, max_length):
    """
    Simulates a brute-force attack on a password.
    
    Args:
        target_password (str): The password to guess.
        max_length (int): The maximum length of the password to attempt.
    
    Returns:
        str: The guessed password if successful.
    """
    # Define the character set to use for the attack (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Try all possible combinations up to the maximum length
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            print(f"Trying: {guess_password}")  # Output the guess for visibility
            if guess_password == target_password:
                return f"Password found: {guess_password}"
    
    return "Password not found within the maximum length."

# Example usage
if __name__ == "__main__":
    # Set the password to guess
    target_password = "abc"
    
    # Set the maximum length for the brute-force attack
    max_length = 4
    
    result = brute_force_attack(target_password, max_length)
    print(result)
