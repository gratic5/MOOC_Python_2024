# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    id_general = 1

    def __init__(self, description : str, programmer : str, workload : int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False
        self.id = Task.id_general
        Task.id_general += 1

    def mark_as_finished(self):
        self.status = True

    def __str__(self):
        str1 = "NOT FINISHED"
        if(self.is_finished()):
            str1 = "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {str1}"

    def is_finished(self):
        return self.status

class Order:

    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def finished_tasks(self):
        return [i for i in self.orders if i.is_finished()]
    
    def unfinished_tasks(self):
        return [i for i in self.orders if not i.is_finished()]
    
    def programmer_names(self):
        a1 = {i.programmers for i in self.orders}
        return list(a1)
    
    def status_of_programmer(self, name):
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        flag = False
        for i in self.orders:
            if(i.programmer == name):
                flag = True
                if(i.is_finished()):
                    a1 += 1
                    a3 += i.workload
                else:
                    a2 += 1
                    a4 += i.workload
        if(flag):
            return f"tasks: finished {a1} not finished {a2}, hours: done {a3} scheduled {a4}"
        return "erroneous input"

class Interface:
    def __init__(self):
        self.interface = Order()

    def start(self):
        print(f"commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")

        while(True):
            print()
            n1 = input("command: ")
            if(n1 == "0"):
                break

            elif(n1 == "1"):
                a1 = input("description: ")
                a2 = input("programmer and the workload estimate: ")
                a3 = a2.split(" ")
                if(len(a3) == 1 or (not a3[1].isdigit())):
                    print("erroneous input")
                    continue
                self.interface.add_order(a1, a3[0],int(a3[1]))
                print("added!")

            elif(n1 == "2"):
                if(self.interface.finished_tasks() == []):
                    print("no finished tasks")
                    continue
                for i in self.interface.finished_tasks():
                    print(i)


            elif(n1 == "3"):
                if(self.interface.unfinished_tasks() == []):
                    print("no unfinished tasks")
                    continue
                for i in self.interface.unfinished_tasks():
                    print(i)

            elif(n1 == "4"):
                b1 = input("id: ")
                if(not b1.isdigit()):
                    print("erroneous input")
                    continue
                flag = False
                for i in self.interface.orders:
                    if(i.id == int(b1)):
                        flag = True
                        i.mark_as_finished()
                if(flag):
                    print("marked as finished")
                    continue
                else:
                    print("erroneous input")
                    continue
            
            elif(n1 == "5"):
                c1 = {i.programmer for i in self.interface.orders}
                for i1 in c1:
                    print(i1)
            
            elif(n1 == "6"):
                d1 = input("programmer: ")
                print(self.interface.status_of_programmer(d1))

i1 = Interface()
i1.start()