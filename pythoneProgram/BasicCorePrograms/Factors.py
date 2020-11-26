"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${10:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - Computes the prime factorization of N using brute force.
"""
import math

class factors :

    # constructor
    def __init__(self, userNumber) :
        self.userNumber = userNumber
        self.factor = 1

    # method for calculating prime factor
    def calculateFactor(self) :
        # print the two and divide by two if remainder is zero
        while self.userNumber % 2 == 0:
            print ('2'),
            self.userNumber = self.userNumber / 2
        # find square root and increment by 2 in range of 3 to squareroot value
        for i in range(3, int(math.sqrt(self.userNumber)) + 1, 2):
            while self.userNumber % i == 0:
                print(i)
                self.userNumber = self.userNumber / i
        # some time prime factor remaining at last so tat will print
        if self.userNumber >2 :
            print(int(self.userNumber))


# main
if __name__ == '__main__' :
    # Exception Handling
    try:
        # accepting Number from User
        userNumber = int(input('Enter a number : '))
        # creating object and pass Parameter
        factorsObject = factors(userNumber)
        # Calling Method CalculateFactor
        factorsObject.calculateFactor()
    except :
        print('Exception Raised.')