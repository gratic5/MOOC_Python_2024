# Write your solution here:

class Task:
    id_main = 1

    def __init__(self, description : str, programmer : str, workload : int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.task_status = False
        self.id = Task.id_main
        Task.id_main += 1
        

    def __str__(self):
        str1 = "NOT FINISHED"
        if(self.task_status):
            str1 = "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {str1}"
    
    def is_finished(self):
        return self.task_status

    def mark_finished(self):
        self.task_status = True


class OrderBook:

    def __init__(self):
        self.orders = []

    def add_order(self, description, name, workload):
        self.orders.append(Task(description, name, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        a1 = {i.programmer for i in self.orders}
        return list(a1)
        
    def mark_finished(self, id : int):
        flag = False
        for i in self.orders:
            if i.id == id:
                i.mark_finished()
                flag = True
        if(not flag):
            raise ValueError
        
    def finished_orders(self):
        return [i for i in self.orders if i.is_finished()]
    
    def unfinished_orders(self):
        return [i for i in self.orders if not i.is_finished()]

    def status_of_programmer(self, programmer : str):
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        flag = False
        for i in self.orders:
            if(i.programmer == programmer):
                flag = True
                if(i.is_finished()):
                    a1 += 1
                    a3 += i.workload
                else:
                    a2 += 1
                    a4 += i.workload
        if(not flag):
            raise ValueError
        return (a1,a2,a3,a4)

