## FUNCTION: inputData

class Matrix:

    def __init__ (self):
    #     self.row = 0
    #     self.col = 0

    # def inputData(self):
        # enter number of matrix rows and columns
        self.row = int(input("Enter number of rows: "))
        self.col = int(input("Enter number of columns: "))
        # enter matrix elements
        self.matrix = []
        for i in range(self.row):
            temp = []
            for j in range(self.col):
                temp.append(int(input(("Enter Element [{}][{}]: ").format(i+1, j+1))))
            self.matrix.append(temp)

    ## FUNCTION: print

    def print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], end = ' ')
            print()

    ## FUNCTION: add

# main 
matrix1 = Matrix()
matrix1.print()

matrix2 = Matrix()
matrix2.print()

matrix1 + matrix2