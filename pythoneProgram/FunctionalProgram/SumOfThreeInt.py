"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${12:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
"""


class sumOfThreeInt :

    # constructor
    def __init__(self) :
        self.listLenght = 0
        self.list = []
        self.flag = False

    # Accepting List Number
    def acceptingListValue(self):
        self.listLenght = int(input('How many element you wnat to enter :'))
        print('Enter the number :')
        for i in range(self.listLenght) :
            self.list.append(int(input()))
        print (self.list)

    # Find Triplate Method
    def findTriplets(self):
        found = False
        for i in range(0, self.listLenght - 2):
            for j in range(i + 1, self.listLenght - 1):
                for k in range(j + 1, self.listLenght):
                    if (self.list[i] + self.list[j] + self.list[k] == 0):
                        # Print Triplets
                        print(self.list[i], self.list[j], self.list[k])
                        found = True
        # If no triplet with 0 sum found in array
        if found == False:
            print("not exist ")


# main
if __name__ == '__main__' :
    # Exception Handling
    try :
        # creating object
        sumOfThreeIntobject = sumOfThreeInt()
        # Calling Method AcceptingListValue
        sumOfThreeIntobject.acceptingListValue()
        # Calling Method FindTriplets
        sumOfThreeIntobject.findTriplets()
    except :
        print('Exception Raised.')