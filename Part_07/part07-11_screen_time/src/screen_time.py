# Write your solution here
import datetime



filename = input("Filename: ")
starting_date = input("Starting date: ")
period = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
starting_date_object = datetime.datetime.strptime(starting_date, "%d.%m.%Y")
final_date = starting_date_object + datetime.timedelta(period-1)

list1 = []
for i in range(period):
    dict1 = {}
    resulting_date_object = datetime.timedelta(days=i) + starting_date_object
    
    screen_time = input(f"Screen time {datetime.datetime.strftime(resulting_date_object,"%d.%m.%Y")} ")
    final_screen_time = screen_time.split(" ")

    dict1[resulting_date_object] = final_screen_time
    list1.append(dict1)

sum1 = 0
average_minutes = 0
for i,j in enumerate(list1):
    for k,v in j.items():
        l1 = [int(x) for x in v]
        sum1 += sum(l1)
average_minutes = sum1/len(list1)

with open(filename,"w") as d:
    d.write(f"Time period: {datetime.datetime.strftime(starting_date_object,"%d.%m.%Y")}-{datetime.datetime.strftime(final_date,"%d.%m.%Y")}\n")
    d.write(f"Total minutes: {sum1}\n")
    d.write(f"Average minutes: {average_minutes:.1f}\n")
    for i,j in enumerate(list1):
        for k,v in j.items():
            d.write(f"{datetime.datetime.strftime(k,"%d.%m.%Y")}: {v[0]}/{v[1]}/{v[2]}\n")

print(f"Data stored in file {filename}")