
# Write your solution here:
class Person:

    def __init__(self, name : str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def add_number(self, number : str):
        self.__numbers.append(number)

    def add_address(self, address : str):
        self.__address = address 

    def name(self):
        return self.__name 
    
    def address(self):
        return self.__address
    
    def numbers(self):
        return self.__numbers

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def __get_name(self, name : str):
        if(name in self.__persons):
            return name
        return None

    def add_number(self, name: str, number: str):
        if(self.__get_name(name) is None):
            p1 = Person(name)
            p1.add_number(number)
            self.__persons[name] = p1
        else:
            self.__persons[name].add_number(number)

    def add_address(self, name : str, address : str):
        if(name in self.__persons):
            self.__persons[name].add_address(address)
        else:
            p1 = Person(name)
            p1.add_address(address)
            self.__persons[name] = p1

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

    def search_by_name(self):
        name = input("name: ")
        n1 = self.get_entry(name)
        if n1 == None:
            print("number unknown") 
            print("address unknown")
            return 
        elif(n1 is not None):
            if(n1.numbers() == []):
                print("number unknown")
            else:
                for i in n1.numbers():
                    print(i)
            if(n1.address() is None):
                print("address unknown")
            else:
                print(f"{n1.address()}")

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        self.__phonebook.search_by_name()

    def add_address(self):
        name = input("name ") 
        address = input("address: ") 
        self.__phonebook.add_address(name, address)    

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
