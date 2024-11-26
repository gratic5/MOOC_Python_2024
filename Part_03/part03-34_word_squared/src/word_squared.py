# Write your solution here
def squared(a,b):
    count = 0
    for i in range(b):
        for j in range(b):
            if(count == len(a)):
                count = 0
            print(a[count],end = "")
            count += 1
        print()

if __name__ == "__main__":
    squared("ab",3)

