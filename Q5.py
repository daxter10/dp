import random
import string


def load_dictionary(file_path):
    """Load words from a dictionary file."""
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def shuffle_word(word):
    """Shuffle the letters of a word."""
    return ''.join(random.sample(word, len(word)))


def generate_password(words, max_length=10):
    """Generate a password from a list of words with special characters and a maximum length."""
    if not words:
        return None

    # Define the special characters to use
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    password = ""
    while len(password) < max_length:
        # Choose a random word and shuffle it
        word = random.choice(words)
        shuffled_word = shuffle_word(word)

        # If adding the next shuffled word would exceed the length limit, cut it short
        if len(password) + len(shuffled_word) > max_length:
            remaining_length = max_length - len(password)
            shuffled_word = shuffled_word[:remaining_length]

        password += shuffled_word

        # Randomly add special characters
        if len(password) < max_length:
            # Choose a random special character
            special_char = random.choice(special_characters)
            password += special_char

        # Trim the password to the max length if it exceeds it
        password = password[:max_length]

    return password


def main():
    # Path to your dictionary file
    dictionary_file = 'dictionary.txt'

    # Load the words from the dictionary file
    words = load_dictionary(dictionary_file)

    # Generate a password
    if words:
        password = generate_password(words, max_length=10)
        if password:
            print(f"Generated Password: {password}")
        else:
            print("Failed to generate a password.")
    else:
        print("No words available for password generation.")


if __name__ == "__main__":
    main()
