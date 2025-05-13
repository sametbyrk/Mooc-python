def read_matrix():
    matrix = []
    with open("matrix.txt", "r") as file:
        for line in file:
            row = line.strip().split(",")
            int_row = [int(value) for value in row]
            matrix.append(int_row)
    return matrix

def matrix_sum():
    mat = read_matrix()
    total = 0
    for row in mat:
        total += sum(row)
    return total

def matrix_max():
    mat = read_matrix()
    max_val = mat[0][0]
    for row in mat:
        row_max = max(row)
        if row_max > max_val:
            max_val = row_max
    return max_val

def row_sums():

    mat = read_matrix()
    return [sum(row) for row in mat]
