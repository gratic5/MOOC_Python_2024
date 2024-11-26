# Copy here code of line function from previous exercise and use it in your solution
def line(a,b):
    if(b == ""):
        print(f"{'*'*a}")
    else:
        print(b[0]*a)
def shape(w,x,y,z):
    for i in range(1,w+1):
        line(i,x)
    for j in range(y):
        line(w,z)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")