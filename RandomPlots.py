def testing_adjacent_elements(current_list, prev_list, prev_list_start, n_rows):
    len_list = len(current_list)
    current_list_end = len_list - prev_list_start
    for i, j in zip(range(prev_list_start, len_list), range(current_list_end)):
        if i == prev_list_start:
            if prev_list[i] == current_list[j] or prev_list[i] == current_list[j+1]:
                return False
        elif i == (len_list - 1) and current_list_end == n_rows:
            if prev_list[i] == current_list[j-1] or prev_list[i] == current_list[j]:
                return False
        else:
            if prev_list[i] == current_list[j-1] or prev_list[i] == current_list[j] or prev_list[i] == current_list[j+1]:
                return False
    return True

import random
import math
import numpy as np
import sys
# n_reps = 3
# n_plots = 10
# n_cols = 2
n_reps = int(input("Please enter the number of repetitions: "))
print("you entered", n_reps)
n_plots = int(input("Please enter the number of plots: "))
print("you entered", n_plots)
n_cols = int(input("Please enter the number of columns: "))
print("you entered", n_plots)

n_rows = int(math.ceil(float(n_plots)/n_cols))
print("The number of rows will be", n_rows)

n_adjacent_start = n_rows*(n_cols - 1)
# For cases like n_cols = 4 and n_plots = 9 (better n_cols = 3)
if n_plots == n_adjacent_start:
    n_cols -= 1
    n_adjacent_start = n_rows*(n_cols - 1)

print("Cols: " + str(n_cols))
print("Rows: " + str(n_rows))
prev_list = []
current_list = range(1,n_plots+1)
for i in range(n_reps):
    current_list = random.sample(current_list, len(current_list))
    if len(prev_list)!=0:
        while(testing_adjacent_elements(current_list, prev_list, n_adjacent_start, n_rows) == False):
            current_list = random.sample(current_list, len(current_list))
    prev_list = current_list
#     print(current_list)

    array = np.asarray(current_list)
    # Adding None if it's not a perfect matrix
    none_array = np.full(n_rows*n_cols - len(current_list), "Filler")
    array = np.append(array, none_array)
    # spliting to transform to matrix
    array = np.split(array, n_cols)
    # transform into matrix
    matrix = np.matrix(array)
    matrix_transposed = np.matrix.transpose(matrix)

    print("-------------------")
    print("Rep:", i+1)
#     print matrix_transposed
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix_transposed]))
