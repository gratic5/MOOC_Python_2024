import string, random

def generate_strong_password(a : int, b : bool, c : bool):
    password = ""
    password += random.choice(string.ascii_lowercase)
    
    collective_string = string.ascii_lowercase

    if(b):
        password += random.choice(string.digits)
        collective_string += string.digits
    if(c):
        password += random.choice("!?=+-()#")
        collective_string += "!?=+-()#"
    
    while(len(password) < a):
        password += random.choice(collective_string)
    
    password1 = random.sample(password,len(password))
    password2 = ""
    for i in password1:
        password2 += i
    
    return password2
