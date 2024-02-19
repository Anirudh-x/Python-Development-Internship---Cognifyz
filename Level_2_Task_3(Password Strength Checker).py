# Password Strength Checker

def validate(password):

    if len(password) < 12: # Check if password has atleast 12 letters
        return False
    
    if not any(char.isupper() for char in password): # Check if password contains any uppercase
        return False
    
    if not any(char.islower() for char in password): # Check if password contains any lowercase
        return False
    
    if not any(char.isdigit() for char in password): # Check if password contains any digit
        return False
    
    if not any(not char.isalnum() for char in password): # Check if password does not contains any alphanumeric (contains special character)
        return False

    return True 

password = input("\nEnter Password to Check : ") 
check = validate(password)
if check:
    print("Strong Password !")
else:
    print("Weak Password !")