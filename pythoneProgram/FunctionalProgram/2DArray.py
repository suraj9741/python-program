"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${11:50 PM}
   * package - ${PACKAGE_NAME}
   * Title - A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
"""

class twoDArray :

    # constructor
    def __init__(self, row, column) :
        self.row = row
        self.column = column
        print(f'row = {self.row}, column = {self.column}')

    # Enter Value in 2D Array
    def enterTheValue(self):
        twodArray =[]
        print("Enter the entries rowwise : ")
        # A for loop for row entries
        for i in range(self.row):
            print ((i+1),' Row')
            a = []
            # A for loop for column entries
            for j in range(self.column):
                value = int(input())
                a.append(value)
            twodArray.append(a)
        #  Calling Method PrintTwodArray
        self.printTwodArray(twodArray)

    # Printing 2D Array
    def printTwodArray(self,twodArray):
        for i in range(self.row):
            for j in range(self.column):
                print(twodArray[i][j], end = " ")
            print()


# main
if __name__ == '__main__' :
    # Exception Handling
    while True:
        try:
            while True:
                # accepting Row Number from User
                row = int(input('Enter the number of Rows : '))
                if row > 0:
                    break
                else:
                    print('You enter Less than 0 row value.\nEnter again')
            while True:
                # accepting Column Number from User
                column = int(input('Enter the number of Columns : '))
                if column > 0:
                    break
                else:
                    print('You enter Less than 0 column value.\nEnter again')
            # creating object and pass Parameter
            object = twoDArray(row, column)
            # Calling Method EnterTheValue
            object.enterTheValue()
            break
        except ValueError:
            print('You enter str must enter int value')