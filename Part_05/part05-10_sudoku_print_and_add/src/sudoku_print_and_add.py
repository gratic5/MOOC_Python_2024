# Write your solution here
def print_sudoku(sudoku : list):
    for i,j in enumerate(sudoku):
        for k,l in enumerate(sudoku[i]):
            if(l == 0):
                print("_",end = " ")
                if(k == 2 or k == 5):
                    print(" ",end = "")
            else:
                print(l,end = " ")
                if(k == 2 or k == 5):
                    print(" ",end = "")
        print()
        if(i == 2 or i == 5):
            print()

def add_number(sudoku : list, row_no : int, column_no: int, number : int):
    sudoku[row_no][column_no] = number
