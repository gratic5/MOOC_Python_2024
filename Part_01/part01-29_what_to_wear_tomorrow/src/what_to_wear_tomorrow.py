# Write your solution here
print(f"What is the weather forecast for tomorrow?")
n1 = int(input("Temperature: "))
n2 = input("Will it rain (yes/no): ")

if(n1 <= 20):
    print(f"Wear jeans and a T-shirt\nI recommend a jumper as well")
    if(n1 <= 10):
        print(f"Take a jacket with you")
        if(n1 <= 5):
            print(f"Make it a warm coat, actually\nI think gloves are in order")
            if(n2 == "yes"):
                print("Don't forget your umbrella!")
        else:
            if(n2 == "yes"):
                print(f"Don't forget your umbrella!")
    else:
        if(n2 == "yes"):
            print(f"Don't forget your umbrella!")
else:
    print(f"Wear jeans and a T-shirt")
    if(n2 == "yes"):
        print(f"Don't forget your umbrella!")



    
