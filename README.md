# Checksum Password Generator

A script to generate a password that matches a given checksum.

## Description

This script generates a password whose ASCII values sum up to a specified checksum. It can be useful for various applications where a specific checksum is required for security or validation purposes.

The script works as follows:
1. It calculates the sum of the ASCII values of the characters in the provided username.
2. It subtracts this sum from the given checksum to determine the required sum of the ASCII values for the password.
3. It generates a password whose ASCII values sum up to this required value.

In other words:
- `CHECKSUM = USER_NAME ascii + PASSWORD ascii`
- `CHECKSUM - USER_NAME ascii = PASSWORD ascii sum`

### Note
The script has a limit of `max_attempts = 100000` to prevent infinite loops. If the script returns "Unable to find a matching password within the attempt limit," you may need to increase this value, especially if you are working with a large checksum.

## Requirements
* Python 3.x
  
## Usage

To run the script, use the following command:

```sh
python checksum_password_generator.py <username> <checksum>
