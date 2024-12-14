# Write your solution here

import string, random

def generate_password(a : int):
    l1 = list(string.ascii_lowercase)
    password= ""
    for i in range(a):
        password += random.choice(l1)
    return password
