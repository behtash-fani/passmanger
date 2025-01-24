def validate_input(prompt, validator=None):
    """Validate user input based on a validator function."""
    while True:
        user_input = input(prompt).strip()
        if validator and not validator(user_input):
            print("Invalid input. Please try again.")
        else:
            return user_input

def validate_app_name(app_name):
    """Validate the app name."""
    return len(app_name) > 0

def validate_password(password):
    """Validate the password."""
    return len(password) >= 8  # Example: Ensure password is at least 8 characters long