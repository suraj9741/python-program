"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${12:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Flip Coin and print percentage of Heads and Tails.
"""
import random

class flipCoin :
    # constructor
    def __init__(self):
        self.flipCoinNumber = 0
        self.headTail = 0
        self.head = 0
        self.tail =0

    # Coin flip Method
    def numberOfTimeFlipCoin (self):
        self.flipCoinNumber = random.randint(5,10)
        print(self.flipCoinNumber,' Time coin flipped : ')
        for x in range(self.flipCoinNumber):
            self.headTail = random.randint(0,1)
            if self.headTail == 0 :
                print('Round ' + str(x+1) + ' H Win')
                self.head = self.head + 1
            else :
                print('Round ' + str(x+1) + ' T Win')
                self.tail = self.tail + 1
        return self.flipCoinNumber, self.head, self.tail

    # Calculateing Peecentage of Head and Tail
    def CalculatePercentage (self):
        self.flipCoinNumber, self.head, self.tail = self.numberOfTimeFlipCoin()
        self.head = self.head / self.flipCoinNumber * 100
        self.tail = self.tail / self.flipCoinNumber * 100
        print('Head percentage = ' + str(self.head))
        print('Tail percentage = ' + str(self.tail))

    randomNumber = random.randint(1,9)

# Main Method
if __name__ =='__main__' :

    # Exception Handling
    try :
        # Creating object
        flipCoinObject = flipCoin()
        # Calling CalculatePercentage Method
        flipCoinObject.CalculatePercentage()
    except :
        print('Exception Occure')