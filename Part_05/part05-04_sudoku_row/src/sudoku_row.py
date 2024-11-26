# Write your solution here
def row_correct(sudoku : list, row_no : int):
    new_row = []
    for i in sudoku[row_no]:
        if(i not in new_row and i != 0):
            new_row.append(i)
        elif(i in new_row and i != 0):
            return False
    return True
        