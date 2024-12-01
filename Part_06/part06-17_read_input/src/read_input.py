# Write your solution here
def read_input(a , b, c):
    while(True):
        try:
            a1 = int(input(a))
            if(a1 >= b and a1 <= c):
                return a1
        except:
            pass
        print(f"You must type in an integer between {b} and {c}")