s = str(input("Enter a string: "))
if s.isalnum():
    print("This is what i found about that string: ")
    print("The string is alphanumeric.")
if s.isalpha():
    print("The sting contains only alphabetic characters.")
if s.isnumeric():
    print("The string contains only digits.")
if s.islower():
    print("The letter in the string are all lowercase.")
if s.isupper():
    print("The letter in the string are all uppercase.")