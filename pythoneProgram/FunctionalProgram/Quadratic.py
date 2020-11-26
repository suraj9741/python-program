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

    def acceptingValue(self) :
        while True:
            # Accepting a from equation
            a = int(input('Enter a in ( aX^2 + bX + c ) : '))
            if a == 0:
                print('You enter 0 not valid its not Quadratic equation')
            else:
                break
        # Accepting b from equation
        b = int(input('Enter b in ( aX^2 + bX + c ) : '))
        # Accepting c from equation
        c = int(input('Enter c in ( aX^2 + bX + c ) : '))
        # print equation
        print(f'Equation is : {a}X^2 + {b}X + {c}')
        return a, b, c


    def calculation(self, a, b, c) :
        # Calculate delta
        delta = (b * b) - (4 * a * c)
        # Calculate Root 1
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        # Calculate Root 2
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Delta is {delta} \nRoot 1 of x : {root1} \nRoot 2 of x : {root2}')


# main
if __name__ == '__main__' :
    while True:
        # Exception Handling
        try :
            # creating object
            quadraticObject = quadratic()
            # Calling Method AcceptingValue
            a, b, c = quadraticObject.acceptingValue()
            # Calling Method Calculation
            quadraticObject.calculation(a, b, c)
            break
        except ValueError:
            print('You enter str must enter int value')