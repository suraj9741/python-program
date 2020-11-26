"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N.
"""


class harmonicNumber :

    # constructor
    def __init__(self, userNumber):
        self.userNumber = userNumber
        self.div = 0
        self.sum = 0

    # Harmonic Value Calculater
    def harmonicValue(self):
        for i in range(1,(self.userNumber+1)):
            self.div = 1/i
            self.sum = self.sum + self.div
        print(self.sum)


# Main Method
if __name__ == '__main__' :
    # Exception Handling
    try:
        # accepting Number from User
        userNumber = int(input('Enter the number upto you want to print harmonic value :'))
        # creating object and pass Parameter
        harmonicNumberObject = harmonicNumber(userNumber)
        # Calling Method HarmonicValue
        harmonicNumberObject.harmonicValue()
    except:
        print('Exception Raised.')