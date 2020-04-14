import random
import moveLogic
import copy


class Game2048:
    def __init__(self):
        self.__matrix = []
        self.__mcopy = []
        self.__score = 0

    def setCanves(self):
        for i in range(4):
            self.__matrix.append([])
            for j in range(4):
                self.__matrix[i].append(0)
        for i in range(2):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            self.__matrix[x][y] = random.choice([2, 4])
        # for m in self.__matrix:
        #     print(' '.join([str(x) for x in m]))
        # print()
        self.__mcopy = copy.deepcopy(self.__matrix)
        return self.__matrix

    def Up(self):
        self.__matrix, self.__score = moveLogic.moveUp(self.__matrix, self.__score)
        self.UpDateCanves()
        return self.__matrix, self.__score

    def Down(self):
        self.__matrix, self.__score = moveLogic.moveDown(self.__matrix, self.__score)
        self.UpDateCanves()
        return self.__matrix, self.__score

    def Left(self):
        self.__matrix, self.__score = moveLogic.moveLeft(self.__matrix, self.__score)
        self.UpDateCanves()
        return self.__matrix, self.__score

    def Right(self):
        self.__matrix, self.__score = moveLogic.moveRight(self.__matrix, self.__score)
        self.UpDateCanves()
        return self.__matrix, self.__score

    def UpDateCanves(self):
        if self.__mcopy != self.__matrix:
            self.__matrix = moveLogic.AddNewNum(self.__matrix)
            self.__mcopy = copy.deepcopy(self.__matrix)
        # for m in self.__matrix:
        #     print(' '.join([str(x) for x in m]))
        # print(self.__score)

    def GameOver(self):
        tempMatrix = copy.deepcopy(self.__matrix)
        if tempMatrix == moveLogic.moveRight(tempMatrix, self.__score)[0]:
            if tempMatrix == moveLogic.moveLeft(tempMatrix, self.__score)[0]:
                if tempMatrix == moveLogic.moveUp(tempMatrix, self.__score)[0]:
                    if tempMatrix == moveLogic.moveDown(tempMatrix, self.__score)[0]:
                        return True
        return False

    def get_score(self):
        return self.__score


# game = Game2048()
# game.setCanves()
#
# while not game.GameOver():
#     op = input("输入移动方向（W上A左S下D右）：")
#     if op == "W":
#         game.Up()
#     elif op == "A":
#         game.Left()
#     elif op == "S":
#         game.Down()
#     elif op == "D":
#         game.Right()
#     else:
#         print("移动方向输入错误！")
# print("游戏结束")
