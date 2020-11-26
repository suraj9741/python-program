"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${9:30 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a program to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there
            are 2 roots.
"""
import math

class quadratic :

    # constructor
    def __init__(self) :
        self.a = 0
        self.b = 0
        self.c = 0
        self.root1 = 0
        self.root2 = 0
        self.delta = 0


    def acceptingValue(self) :
        # Accepting a from equation
        self.a = int(input('Enter a in ( aX^2 + bX + c ) : '))
        # Accepting b from equation
        self.b = int(input('Enter b in ( aX^2 + bX + c ) : '))
        # Accepting c from equation
        self.c = int(input('Enter c in ( aX^2 + bX + c ) : '))
        # print equation
        print(f'Equation is : {self.a}X^2 + {self.b}X + {self.c}')


    def calculation(self) :
        # Calculate delta
        self.delta = (self.b * self.b) - (4 * self.a * self.c)
        # Calculate Root 1
        self.root1 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
        # Calculate Root 2
        self.root2 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
        print(f'Delta is {self.delta} \nRoot 1 of x : {self.root1} \nRoot 2 of x : {self.root2}')


# main
if __name__ == '__main__' :
    # Exception Handling
    try :
        # creating object
        quadraticObject = quadratic()
        # Calling Method AcceptingValue
        quadraticObject.acceptingValue()
        # Calling Method Calculation
        quadraticObject.calculation()
    except :
        print('Exception Raised.')