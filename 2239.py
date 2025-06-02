import sys

input_ = sys.stdin.readline

# sudokuMap = [list(map(int, list(str(input_().rstrip())))) for _ in range(9)]
sudokuMap = [list(int(n) for n in str(input_().rstrip())) for _ in range(9)]

def checkNumbersConflict(numbers: list):
    # check conflict
    checklist = set()
    for n in numbers:
        if (n != 0) and (n not in checklist):
            checklist.add(n)
        else:
            return False
    return True


for i in range(9):
    for j in range(9):
        if sudokuMap[i][j] == 0:
            for k in range(1, 10): # k: 넣을 숫자
                updatedRow = sudokuMap[i][:j] + [k] + sudokuMap[i][j + 1:]
                updatedCol = []
                for l in range(9):
                    if l == i:
                        updatedCol.append(k)
                    else:
                        updatedCol.append(sudokuMap[l][j])
                updatedBox = []
                pointX = (i // 3) * 3
                pointY = (j // 3) * 3
                for l in range(3):
                    for m in range(3):
                        updatedBox.append(sudokuMap[pointX + l][pointY + m])
                updatedBox[pointX + i % 3][pointY + j % 3] = k
                
                if checkNumbersConflict(updatedRow) and checkNumbersConflict(updatedCol) and checkNumbersConflict(updatedBox):
                    # 현재 위치(i, j)의 sudoku 빈 칸에 값 k를 넣는다.
                    
                # ...
                # 만약 이후에 안 될 경우 Backtracking