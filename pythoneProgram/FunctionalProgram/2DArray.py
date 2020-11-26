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
        self.twodArray =[]
        print(self.row, self.column)

    # Enter Value in 2D Array
    def enterTheValue(self):
        print("Enter the entries rowwise : ")
        # A for loop for row entries
        for i in range(self.row):
            print ((i+1),' Row')
            a = []
            # A for loop for column entries
            for j in range(self.column):
                value = int(input())
                a.append(value)
            self.twodArray.append(a)

    # Printing 2D Array
    def printTwodArray(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.twodArray[i][j], end = " ")
            print()


# main
if __name__ == '__main__' :
    # Exception Handling
    try:
        # accepting Row Number from User
        row = int(input('Enter the number of Rows : '))
        # accepting Column Number from User
        column = int(input('Enter the number of Columns : '))
        # creating object and pass Parameter
        object = twoDArray(row, column)
        # Calling Method EnterTheValue
        object.enterTheValue()
        #  Calling Method PrintTwodArray
        object.printTwodArray()
    except :
        print('Exception Raised.')