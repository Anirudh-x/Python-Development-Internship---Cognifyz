# Python Funtion to Reverse the String by Slicing

def rev(string):
    reverse = string[::-1] # start and stop index is empty and step is set to -1 it will iterate sequence in reverse order
    return reverse

input_str = input("Enter String To Reverse : ")
reverse_input = rev(input_str)
print(reverse_input)

