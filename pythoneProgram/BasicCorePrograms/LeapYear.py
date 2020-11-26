"""
   * author - ${Suraj Jadhav}
   * date - ${23-Nov-20}
   * time - ${1:13 AM}
   * package - ${PACKAGE_NAME}
   * Title - Leap Year.
"""

class leapYear :

    # Check user writen Value is 4 digit oe not
    def acceptandCheckDigit(self):
        while True:
            # Accepting Year from user
            year = int(input('Enter Year : '))
            if len(str(year)) == 4:
                # Calling CheckLeapYear Method
                if (self.checkLeapYear(year)):
                    return f'{year} is Leap Year'
                else:
                    return f'{year} is not Leap Year'
            else:
                print(f'{year} is not 4 digit number\nEnter again')


    # Check Leap Year Method
    def checkLeapYear(self,year):
        # Check Year divisible by 4 or not
        if (year % 4) == 0:
            # Check Year divisible by 100 or not
            if (year % 100) == 0:
                # Check Year divisible by 400 or not
                if (year % 400) == 0:
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
    while True:
        try:
            # creating object and pass Parameter
            leapYearObject = leapYear()
            print(leapYearObject.acceptandCheckDigit())
            break
        except ValueError:
            print('You enter str must enter int value')