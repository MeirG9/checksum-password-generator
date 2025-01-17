import random
import string
import argparse

def find_password(sum_of_predict_password):
    """
    Generate a random password that matches the given sum of ASCII values.

    Args:
    sum_of_predict_password (int): The target sum of ASCII values for the password.

    Returns:
    str: A password that matches the target sum.
    """

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    # Attempt to find a matching password
    attempts = 0
    max_attempts = 100000  # Set a limit to prevent infinite loop
    while attempts < max_attempts:
        # Generate a random password of length 1 to 12
        password_length = random.randint(1, 12)
        password = ''.join(random.choice(chars) for _ in range(password_length))
        sums = sum(ord(c) for c in password)
        if sum_of_predict_password == sums:
            return password
        attempts += 1
    raise ValueError("Unable to find a matching password within the attempt limit.")

def main():
    try:
        parser = argparse.ArgumentParser(description="Generate a password that matches a given checksum.")
        parser.add_argument("username", type=str, help="The username to calculate the checksum for.")
        parser.add_argument("checksum", type=int, help="The target checksum value.")

        args = parser.parse_args()

        # Calculate the sum of the ASCII values of the characters in the username
        username_sum = sum(ord(c) for c in args.username)

        # Calculate the password sum needed to match the target checksum
        password_sum = args.checksum - username_sum

        print(f"Password sum needed: {password_sum}")
        password = find_password(password_sum)
        print(f"Password found: {password}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred! : {e}")

if __name__ == "__main__":
    main()