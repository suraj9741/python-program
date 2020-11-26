"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${1:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Leap Year.
"""
class leapYear :

    # constructor
    def __init__(self, year) :
        self.year = year

    # Check user writen Value is 4 digit oe not
    def checkDigit(self):
        if len(str(self.year)) == 4:
            # Calling CheckLeapYear Method
            if (self.checkLeapYear()):
                return f'{self.year} is Leap Year'
            else :
                return f'{self.year} is not Leap Year'
        else :
            return f'{self.year} is not 4 digit number'

    # Check Leap Year Method
    def checkLeapYear(self):
        # Check Year divisible by 4 or not
        if (self.year % 4) == 0:
            # Check Year divisible by 100 or not
            if (self.year % 100) == 0:
                # Check Year divisible by 400 or not
                if (self.year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


# Main Method
if __name__ == '__main__' :
    # Exception Handling
    try :
        # Accepting Year from user
        year = int(input('Enter Year : '))
        # creating object and pass Parameter
        leapYearObject = leapYear(year)
        print(leapYearObject.checkDigit())
    except :
        print('Exception Raised.')