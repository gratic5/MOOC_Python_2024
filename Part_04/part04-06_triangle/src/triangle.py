# Copy here code of line function from previous exercise
def line(a,b):
    if(b == ""):
        print(f"{'*'*a}")
    else:
        print(b[0]*a)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1,size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
