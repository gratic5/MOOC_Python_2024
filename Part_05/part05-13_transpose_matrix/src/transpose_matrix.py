# Write your solution here
def transpose(matrix : list):
    new_matrix = []
    count = 0
    for i,j in enumerate(matrix):
        new_row = []
        for k,l in enumerate(matrix):
            new_row.append(matrix[k][i])
        new_matrix.append(new_row)
    matrix[:] = new_matrix

