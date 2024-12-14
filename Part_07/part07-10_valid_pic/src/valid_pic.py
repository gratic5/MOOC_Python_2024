# Write your solution here
import datetime

def is_it_valid(pic : str) -> bool:
    if(pic[6] not in "+-A"):
            return False
    
    if(len(pic) > 11):
        return False
    
    number = ""
    if(pic[6] == "+"):
        year = f"18{pic[4]}{pic[5]}"
        number = year
        try:
            datetime.date(int(year),int(pic[2]+pic[3]),int(pic[0]+pic[1]))
        except:
            return False
    elif(pic[6] == "-"):
        year = f"19{pic[4]}{pic[5]}"
        number = year
        try:
            datetime.date(int(year),int(pic[2]+pic[3]),int(pic[0]+pic[1]))
        except:
            return False
    elif(pic[6] == "A"):
        year = f"20{pic[4]}{pic[5]}"
        number = year
        try:
            datetime.date(int(year),int(pic[2]+pic[3]),int(pic[0]+pic[1]))
        except:
            return False
    
    control_character_list = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_character_index = int(pic[:6] + pic[7:10]) % 31

    if(pic[10] == control_character_list[control_character_index]):
        return True
    return False
