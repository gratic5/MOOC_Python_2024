# Write your solution here

def copy_and_add(sudoku : list, row_no : int, column_no: int, number : int):
    new_sudoku = []
    for i in sudoku:
        new_row = []
        for j in i:
            new_row.append(j)
        new_sudoku.append(new_row)
    new_sudoku[row_no][column_no] = number
    return new_sudoku
