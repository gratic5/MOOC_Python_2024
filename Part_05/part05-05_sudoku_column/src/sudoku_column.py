# Write your solution here
def column_correct(sudoku : list, column_no : int):
    new_column = []
    for i in sudoku:
        if(i[column_no] in new_column and i[column_no] > 0):
            return False
        new_column.append(i[column_no])
    return True
