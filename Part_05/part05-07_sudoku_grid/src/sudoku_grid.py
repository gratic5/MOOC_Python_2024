# Write your solution here
def row_correct(sudoku : list, a):
    new_row = []
    for i in sudoku[a]:
        if(i in new_row and i > 0):
            return False
        new_row.append(i)
    return True

def column_correct(sudoku : list, b):
    new_column = []
    for i in sudoku:
        if(i[b] in new_column and i[b] > 0):
            return False
        new_column.append(i[b])
    return True

def block_correct(sudoku : list, x , y):
    new_block = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            if(sudoku[i][j] in new_block and sudoku[i][j] > 0):
                return False
            new_block.append(sudoku[i][j])
    return True
    
def sudoku_grid_correct(sudoku : list):
    for i in range(len(sudoku)):
        if(not row_correct(sudoku,i)):
            return False
        
    for i in range(len(sudoku)):
        if(not column_correct(sudoku,i)):
            return False
    
    for i in range(0,7,3):
        for j in range(0,7,3):
            if(not block_correct(sudoku,i,j)):
                return False
    return True


