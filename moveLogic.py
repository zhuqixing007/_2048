import random


def check0(l):
    # 按移动方向将所有非0数排到前面
    flag1 = 1
    while flag1 == 1:
        flag1 = 0
        flag2 = 0
        for i in l:
            if flag2 == 1 and i != 0:
                flag1 = 1  # 0后面出现非0数
            if i == 0:
                flag2 = 1  # 出现0
        if flag1 == 1:
            for i in range(3):
                if l[i] == 0:
                    # 非0数前移
                    l[i] = l[i + 1]
                    l[i + 1] = 0
    return l


def move(l, n):
    l = check0(l)
    for i in range(3):
        if l[i] == l[i + 1]:
            l[i] *= 2
            l[i + 1] = 0
            n += l[i]
    return check0(l), n


def convertMatrix(matrix):
    res = []
    for i in range(4):
        res.append([])
        for j in range(4):
            res[i].append(matrix[j][i])
    return res


def moveLeft(matrix, n):
    for i in range(4):
        matrix[i], n = move(matrix[i], n)
    return matrix, n


def moveRight(matrix, n):
    for i in range(4):
        matrix[i].reverse()
        matrix[i], n = move(matrix[i], n)
        matrix[i].reverse()
    return matrix, n


def moveUp(matrix, n):
    matrix, n = moveLeft(convertMatrix(matrix), n)
    return convertMatrix(matrix), n


def moveDown(matrix, n):
    matrix, n = moveRight(convertMatrix(matrix), n)
    return convertMatrix(matrix), n


def AddNewNum(matrix):
    new_num = random.choice([2, 4])
    positions = []
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                positions.append([i, j])
    if len(positions) > 0:
        position = random.choice(positions)
        matrix[position[0]][position[1]] = new_num
    return matrix
