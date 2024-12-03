import requests
import hashlib

def get_password_hash_suffix(password):
    """Get the SHA-1 hash suffix of the password."""
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1_hash[:5], sha1_hash[5:]

def check_password_in_pwned_api(password):
    """Check if the password has been leaked using the Have I Been Pwned API."""
    prefix, suffix = get_password_hash_suffix(password)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error checking password: {e}")
        return False
    
    hashes = response.text.splitlines()
    return any(suffix == hash_.split(':')[0] for hash_ in hashes)

def process_file(file_path):
    """Process the file to check passwords."""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if ',' not in line:
                print(f"Skipping invalid line: {line}")
                continue
            
            username, password = map(str.strip, line.split(',', 1))
            if check_password_in_pwned_api(password):
                print(f"Password for user '{username}' has been leaked.")
            else:
                print(f"Password for user '{username}' is safe.")

if __name__ == "__main__":
    file_path = 'user_passwords.txt'  # Update with your file path
    process_file(file_path)
