"""
   * author - ${Suraj Jadhav}
   * date - ${22-Nov-20}
   * time - ${10:55 PM}
   * package - ${PACKAGE_NAME}
   * Title - User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""

import re
class replaceString :

    # constructor
    def __init__(self):
        self.userName = " "

    # Method To Accepting and check the min character condition
    def main(self):
        while True:
            self.userName = input("Enetr the User Name : ")
            regex_name = re.compile(r"^[A-za-z]{1}[A-za-z]{2,}")
            k = regex_name.search(self.userName)
            if k:
                print ('Hello '+ self.userName +', How are you?')
                break
            else:
                print(f'Enter min 3 char.\nyou enter {self.userName}\nEnter againS')

# Main method
if __name__ == '__main__':

    # Exception Handling
    try :
        stringObject = replaceString()
        stringObject.main()
    except :
        print('Exception Raised.')