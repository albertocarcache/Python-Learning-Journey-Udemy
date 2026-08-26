"""
User Registration System

A simple user registration module that demonstrates:
- Validation functions
- Exception handling
- Duplicate checking
- Basic in-memory storage
"""
# ---------------------------------------------------------
# Part 1: Simulated Database
# ---------------------------------------------------------

registered_users = []
# A global list that stores successfully registered users.
# Contains names, emails, passwords, and status: "active".
failed_registrations = []
# A global list that stores information about failed registration attempts.
# Contains emails and error messages.

# ---------------------------------------------------------
# Part 2: Validation Functions
# ---------------------------------------------------------

def validate_name(name: str) -> bool:
    """
    Validate that the name contains at least 3 characters.
    Args:
        name (str): The user's name.
    Returns:
        bool: True if valid, otherwise False.
     """
    return len(name) >= 3                                                                                                                                                                 

def validate_email(email: str) -> bool:
    """
    Validate that the email contains both '@' and '.'.
    Args:
        email (str): The user's email address.
    Returns:
        bool: True if valid, otherwise False.
    """
    return "@" in email and "." in email
       
def validate_password(password: str) -> bool:
    """
    Validate the password strength.
    Rules:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one digit
    Args:
        password (str): The user's password.
    Returns:
        bool: True if valid, otherwise False.
    """
    return len(password) >= 8 and not password.islower() and any(char.isdigit() for char in password)

# ---------------------------------------------------------         
# Part 3: Orchestrator Function - Main Validation Function
# ---------------------------------------------------------

def validate_user_data(name: str, email: str, password: str) -> bool:
    """
    Validate all user inputs.
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
    Returns:
        bool: True if all validations pass.
        list: validation errors
    """
    is_valid = True # boolean variable
    errors = [] # list: validation errors

    if not validate_name(name):
        errors.append(f"The name must contain at least 3 characters: {name}")
        is_valid = False

    if not validate_email(email):
        errors.append(f"The email must contain both (@) and (.): {email}")
        is_valid = False
    
    if not validate_password(password):
        errors.append(f"Password must be at least 8 characters long, contain an uppercase letter and a digit: {password}")
        is_valid = False

    return is_valid, errors

# ---------------------------------------------------------
# Part 4: Registration Function
# ---------------------------------------------------------

def create_user_account(name: str, email: str, password: str):
     """
    Create a new user account after validation.
    Call validate_user_data() to validate the inputs.
    Check whether the email already exists in the registered_users list.
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
    Appends:
       new_user dictionary to the global registered_users list: If registration succeeds.
       fail_user dictionary to the global failed_registrations list: If registration fails. 
    Prints:
        Registration successful & registration data: If registration succeeds.
        Registration failed & the error message: If registration fails.
     """
     format_ok, error_list = validate_user_data(name, email, password) # Unpack variables (is_valid, errors)
     
     is_duplicate = any(user["email"] == email for user in registered_users) # Check for duplicate emails
     
     if format_ok and not is_duplicate:
          new_user = {"name": name, 
                      "email": email, 
                      "password": password,
                      "status": "active"
                     }
          registered_users.append(new_user)
          print(f"Registration successful: {new_user}")
      
     else:
          if is_duplicate:
              error_list.append(f"An account with this email already exists: {email}")

          fail_user = {"email": email, 
                       "error": error_list
                      }                     
          failed_registrations.append(fail_user) 
          print(f"Registration failed: {error_list}")
       
# ---------------------------------------------------------
# Part 5: Testing Implementation
# ---------------------------------------------------------

# Testing the following cases:
# 1) A valid registration
create_user_account("Albert", "albert@email.com", "secure456A")
# 2) A duplicate email
create_user_account("Bruce", "albert@email.com", "pass123IM")
# 3) An invalid name
create_user_account("Jo", "jo@email.com", "secure456B")
# 4) An invalid email
create_user_account("Eddy", "eddymail.com", "pass123A")
# 5) A weak password
create_user_account("Bonjovi", "bonjovi@email.com", "weakpass")
# 6) Another valid registration
create_user_account("RobHalford", "robhalford@email.com", "JProbhalford90")

# Print the final contents of registered_users
print("\nregistered_users:\n", registered_users, sep = "")

# Print the final contents of failed_registrations
print("\nfailed_registrations:\n", failed_registrations, sep = "")










