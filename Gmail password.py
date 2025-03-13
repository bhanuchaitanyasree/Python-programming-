password = input("Enter your password: ")
l = len(password)
special_chars = ['@', '#', '$', '%', '&', '!', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '\\', '^', '~']
if l < 8:
    print("invalid password")
else:
    digit = False
    upper = False
    lower = False
    special = False
    for i in password:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i in special_chars:  
            special = True
    if digit and upper and lower and special:
        print("valid password")
    else:
        print("invalid password")
