# Write your solution here
def store_personal_data(personal : tuple):
    with open("people.csv","a") as p:
        p.write(f"{personal[0]};{personal[1]};{personal[2]}")