# WRITE YOUR SOLUTION HERE:

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list : list):
        dict1 = cls.__dicionary_generator(my_list)
        return max(dict1, key=dict1.get)
            

    @classmethod
    def doubles(cls, my_list : list):
        dict1 = cls.__dicionary_generator(my_list)
        l1 = []
        for i,j in dict1.items():
            if(j > 1):
                l1.append(i)
        return len(l1)
    
    @classmethod
    def __dicionary_generator(cls, l1 : list):
        count = 0
        element = l1[0]

        dict1 = {}
        
        for j in l1:
            for i in l1:
                if(i == element):
                    count += 1
            dict1[element] = count
            count = 0
            element = j
        
        return dict1
