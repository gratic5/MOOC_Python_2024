# Write your solution here
n1 = int(input("Layers: "))
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
right = ""
left = ""
k = n1 -1
m = 2*n1-1

while(k >= 1):
    left = left+alphabets[k]
    right = alphabets[k] + right
    m  -= 2
    print(left +alphabets[k]*m +right)
    k -= 1
while(k <= n1 -1):
    print(left +alphabets[k]*m +right)
    left = left[:-1]
    right = right[1:]
    m +=2
    k +=1



