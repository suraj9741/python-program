"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${12:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Flip Coin and print percentage of Heads and Tails.
"""
import random

class flipCoin :

    # Coin flip Method
    def numberOfTimeFlipCoin (self):
        flipCoinNumber = random.randint(5,10)
        print(flipCoinNumber,' Time coin flipped : ')
        for x in range(flipCoinNumber):
            headTail = random.randint(0,1)
            if headTail == 0 :
                print('Round ' + str(x+1) + ' H Win')
                head = head + 1
            else :
                print('Round ' + str(x+1) + ' T Win')
                tail = tail + 1
        return flipCoinNumber, head, tail

    # Calculateing Peecentage of Head and Tail
    def CalculatePercentage (self):
        flipCoinNumber, head, tail = self.numberOfTimeFlipCoin()
        head = head / flipCoinNumber * 100
        tail = tail / flipCoinNumber * 100
        print('Head percentage = ' + str(head))
        print('Tail percentage = ' + str(tail))

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