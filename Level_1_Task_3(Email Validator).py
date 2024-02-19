# Email Validator

def email_validator(email):
    
    if ('@gmail.' or '@yahoo.' or '@outlook.' or '@hotmail.') in email: # Here if the given email contains any domain taken in ths program then the email is valid
        print("\nEmail is Valid\n")
    else:
        print("\nEmail is Invalid\n")

input_email = input("\nEnter Email : ")
validate = email_validator(input_email)