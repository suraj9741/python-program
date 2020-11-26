"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${8:58 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a program that takes two integer command-line arguments x and y and prints the Euclidean distance from
        the point (x, y) to the origin (0, 0). The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""
import math

class  distance:

    def acceptValue(self) :
        # Accept Y Point
        X2 = int(input('Enter X : '))
        # Accept Y Point
        Y2 = int(input('Enter Y : '))
        return X2, Y2
    def calculateDistance(self, X2, Y2):
        # Euclidean distance Formula
        X1=0
        Y1=0
        distance = math.sqrt(pow((X1-X2), 2) + pow((Y1-Y2), 2))
        print('Distance between two points : ', distance)

# main
if __name__ == '__main__':
    # Exception Handling
    try:
        # creating object
        distanceObject = distance()
        # Calling Method AcceptValue
        X2, Y2 = distanceObject.acceptValue()
        # Calling Method calculateDistance
        distanceObject.calculateDistance(X2, Y2)
    except:
        print('Exception Raised.')