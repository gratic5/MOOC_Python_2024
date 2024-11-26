# Write your solution here
def same_chars(a,b,c):
    if(c > len(a) -1 or (b > (len(a) - 1))):
        return False
    if(a[b] == a[c]):
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))