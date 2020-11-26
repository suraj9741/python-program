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

    # constructor
    def __init__(self) :
        self.X1 = 0
        self.Y1 = 0
        self.X2 = 0
        self.Y2 = 0
        self.distance = 0

    def acceptValue(self) :
        # Accept Y Point
        self.X2 = int(input('Enter X : '))
        # Accept Y Point
        self.Y2 = int(input('Enter Y : '))
    def calculateDistance(self):
        # Euclidean distance Formula
        self.distance = math.sqrt(pow((self.X1-self.X2), 2) + pow((self.Y1-self.Y2), 2))
        print('Distance between two points : ', self.distance)

# main
if __name__ == '__main__':
    # Exception Handling
    try:
        # creating object
        distanceObject = distance()
        # Calling Method AcceptValue
        distanceObject.acceptValue()
        # Calling Method calculateDistance
        distanceObject.calculateDistance()
    except:
        print('Exception Raised.')