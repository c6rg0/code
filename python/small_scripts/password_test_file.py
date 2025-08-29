def check_string(s):
    has_upper = any(char.isupper() for char in s)
    has_lower = any(char.islower() for char in s)
    has_digit = any(char.isdigit() for char in s)
    has_symbol = any(not char.isalnum() for char in s)  # Non-alphanumeric characters

    return has_upper, has_lower, has_digit, has_symbol

# Example usage:
string = "Hello123!"
result = check_string(string)
print(result)  # Output: (True, True, True, True)
