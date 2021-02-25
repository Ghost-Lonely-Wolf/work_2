class Matrix:
    def __init__(self, value_1, value_2):
        self.matr = [value_1, value_2]
        self.value_1 = value_1
        self.value_2 = value_2


    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.value_1)):


            for n in range(len(self.value_2[i])):
                matr[i][n] = self.value_1[i][n] + self.value_2[i][n]


        return str('\n'.join(['\t'.join([str(n) for n in i]) for i in matr]))


my_matrix = Matrix([[-39, 7, 44],
                   [47, 4, 9],
                   [27, 55, 2]],
                   [[36, 7, 25],
                    [53, 1, 88],
                    [66, 5, 14]])


print(my_matrix.__add__())