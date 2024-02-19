# Palindrome Checker

def p_check(string):
    reverse = string[::-1] # To reverse the string
    
    if reverse == string: # To check if the reverse string is equal to original string
        print("\nEntered String is a Palindrome.\n")
    else:
        print("\nEntered String is not a Palindrome.\n")


entered = input("\nEnter the String : ")
check = p_check(entered)
