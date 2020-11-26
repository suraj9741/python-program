"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.
"""

class powerOf2:

    # constructor
    def __init__(self, userNumber):
        self.userNumber = userNumber
        self.power = 1

    # Check the range in between 0 <= Number < 31
    def checkUserNumber(self):
        if 0 <= self.userNumber < 31 :
            # Calling Method PowerTable
            self.powerTable()
        else :
            print('Overflows int / Out of range')

    # Print Power of 2 table
    def powerTable(self):
        for i in range(self.userNumber+1):
            # pow(2,3) = (2*2*2) its power function
            self.power = pow(2,i)
            print(f'2^{i} =',self.power)


# Main Method
if __name__ == '__main__':
    # Exception Handling
    try:
        # accepting Number from User
        userNumber = int(input('Enter the value you want print table : '))
        # creating object and pass Parameter
        powerOf2Object = powerOf2(userNumber)
        # Calling Method CheckUserNumber
        powerOf2Object.checkUserNumber()
    except :
        print('Exception Raised.')