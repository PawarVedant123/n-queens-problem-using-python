n = int(input("Enter value of n: "))
N_Queens = []
CheckBoard = []
for i in range(n):
    temp_col = []
    for j in range(n):
        temp_col.append(0)
    CheckBoard.append(temp_col)

def is_safe(row, col):
    if not is_column_safe(row, col):
        return False
    if not is_right_diagonal_safe(row, col):
        return False
    if not is_left_diagonal_safe(row, col):
        return False
    return True

def is_column_safe(row, col):
    for i in range(row):
        if CheckBoard[i][col] == 1:
            return False
    return True

def is_left_diagonal_safe(row, col):
    i = row
    j = col
    while i >= 0 and j >= 0:
        if CheckBoard[i][j] == 1:
            return False
        i -= 1
        j -= 1
    return True

def is_right_diagonal_safe(row, col):
    i = row
    j = col
    while i >= 0 and j < n:
        if CheckBoard[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def backtrack():
    if not N_Queens:
        print("Program exited.")
        return
    last_row, last_col = N_Queens.pop()
    CheckBoard[last_row][last_col] = 0
    PlaceQueen(last_row, last_col + 1)

def PlaceQueen(row, col):
    if row == n:
        print("Solution found: ")
        for row in CheckBoard:
            print(row)
        return
    for j in range(col, n):
        if is_safe(row, j):
            CheckBoard[row][j] = 1
            N_Queens.append((row, j))
            PlaceQueen(row + 1, 0)
            CheckBoard[row][j] = 0
            N_Queens.pop()
    backtrack()

PlaceQueen(0, 0)
