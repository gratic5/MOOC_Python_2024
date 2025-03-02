# WRITE YOUR SOLUTION HERE:

def filter_forbidden(string : str, forbidden : str):
    return "".join([i for i in list(string) if i not in forbidden])
