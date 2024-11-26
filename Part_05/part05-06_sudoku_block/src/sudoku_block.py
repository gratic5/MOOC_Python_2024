# Write your solution here
def block_correct(sudoku : list, row_no : int, column_no : int):
    new_block = []
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            if(sudoku[i][j] in new_block and sudoku[i][j] > 0):
                return False
            new_block.append(sudoku[i][j])
    return True
