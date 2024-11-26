# Write your solution here
def dict_of_numbers():
    d1 = {}
    units = ["one","two","three","four","five","six","seven","eight","nine"]
    tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    unittens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    d1[0] = "zero"
    for i in range(9):
        d1[i+1] = units[i]
    for s in range(10,20):
        d1[s] = tens[s-10]
    for j in range(20,100):
        if(j % 10 == 0):
            a = j // 10
            d1[j] = unittens[a-2]
        else:
            k = j // 10
            h = j % 10
            d1[j] = unittens[k-2] + "-" + units[h-1]
    return d1
    