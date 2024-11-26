# Write your solution here
def chessboard(a):
    for i in range(a):
        for j in range(a):
            if((i+j) % 2 == 0):
                print(1,end = "")
            else:
                print(0,end = "")
        print()
# Testing the function
if __name__ == "__main__":
    chessboard(3)
