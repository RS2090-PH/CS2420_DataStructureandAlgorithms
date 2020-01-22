from arrays import Array
from grid import Grid

class Matrix(object):
    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fillValue)

    def getHeight(self):
        """Returns the number of rows."""
        return len(self.data)

    def getWidth(self):
        "Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [][]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result

    def __add__(self, val_b):
        if (self.getHeight(), self.getWidth()) != (val_b.getHeight(), val_b.getWidth()):
            raise ValueError("Matrix value addition Undefined.")
        else:
            temp = Matrix(self.getHeight(), self.getWidth())
            for row in range(self.getHeight()):
                for column in range(self.getWidth()):
                    temp[row][column] = self.data[row][column] + val_b[row][column]
            return temp

    def __sub__(self, val_b):
        if (self.getHeight(), self.getWidth()) != (val_b.getHeight(), val_b.getWidth()):
            raise ValueError("Matrix value subtraction Undefined.")
        else:
            temp = Matrix(self.getHeight(), self.getWidth())
            for row in range(self.getHeight()):
                for column in range(self.getWidth()):
                    temp[row][column] = self.data[row][column] - val_b[row][column]
            return temp

    def __mul__(self, val_b):
        """ This is incomplete """
        if (self.getHeight(), self.getWidth()) != (val_b.getWidth(), val_b.getHeight()):
            raise ValueError("Matrix value multiplication Undefined.")
        else:
            temp = Matrix(self.getHeight(), self.getHeight())
            for row in range(self.getHeight()):
                for column in range(self.getWidth()):
                    temp[row][column] = self.data[row][column] - val_b[row][column]
            return temp


def main():
    m1 = Matrix(3, 3, 2)
    m2 = Matrix(3, 3, 4)
    print(m1 + m2)
    m1 = Matrix(4, 4, 2)
    m2 = Matrix(4, 4, 4)
    print(m2 - m1)
    m1 = Matrix(2, 3, 2)
    m2 = Matrix(3, 2, 4)
    print(m1 * m2)

if __name__ == "__main__": main()
