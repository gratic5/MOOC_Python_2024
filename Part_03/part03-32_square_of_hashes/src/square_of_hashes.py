# Write your solution here
def hash_square(length):
    for i in range(length):
        for i in range(length):
            print('#',end = "")
        print()
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)