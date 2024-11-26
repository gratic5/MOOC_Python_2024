# Write your solution here
def line(a,b):
    if(b == ""):
        print(f"{'*'*a}")
    else:
        print(b[0]*a)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")