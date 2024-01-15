def solution(arr):
    row = len(arr) 
    column = len(arr[0])
    if row > column:
        for i in range(row):
            arr[i] += ([0] * (row - column))
    elif column > row:
        arr += [([0] * column)] * (column - row)
    return arr 

# print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
# print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))