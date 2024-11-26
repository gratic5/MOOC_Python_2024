# Write your solution here

def spruce(x):
    print("a spruce!")
    for i in range(1,x+1):
        print(f"{(x-i)*' '}{'*'*((2*i)-1)}")
    print(f"{(x-1)*' '}*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)