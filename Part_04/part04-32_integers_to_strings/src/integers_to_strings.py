# Write your solution here
def formatted(a : list) -> list:
    new_list = []
    for i in a:
        new_list.append(f"{i:.2f}")
    return new_list