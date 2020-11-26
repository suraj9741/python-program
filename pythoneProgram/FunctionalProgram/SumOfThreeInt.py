"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${12:50 AM}
   * package - ${PACKAGE_NAME}
   * Title - A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
"""


class sumOfThreeInt :

    # Accepting List Number
    def acceptingListValue(self):
        list = []
        while True:
            listLength = int(input('How many element you want to enter :'))
            if listLength > 0:
                break
            else:
                print('Array cannot be less than 0 so enter greater value.')
        print('Enter the number :')
        for i in range(listLength):
            list.append(int(input()))
        # [0, -1, 2, -3, 1]
        print(list)
        return listLength, list

    # Find Triplate Method
    def findTriplets(self, listLength,list):
        found = False
        for i in range(0, listLength - 2):
            for j in range(i + 1, listLength - 1):
                for k in range(j + 1, listLength):
                    if (list[i] + list[j] + list[k] == 0):
                        # Print Triplets
                        print(list[i], list[j], list[k])
                        found = True
        # If no triplet with 0 sum found in array
        if found == False:
            print("not exist ")


# main
if __name__ == '__main__' :
    while True:
        # Exception Handling
        try :
            # creating object
            sumOfThreeIntobject = sumOfThreeInt()
            # Calling Method AcceptingListValue
            listLength, list = sumOfThreeIntobject.acceptingListValue()
            # Calling Method FindTriplets
            sumOfThreeIntobject.findTriplets(listLength, list)
            break
        except ValueError:
            print('You enter str must enter int value')