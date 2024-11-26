# Write your solution here
def anagrams(a : str, b : str):
    if(sorted(a) == sorted(b)):
        return True
    return False


