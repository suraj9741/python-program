"""
   * author - ${Suraj Jadhav}
   * date - ${22-Nov-20}
   * time - ${10:55 PM}
   * package - ${PACKAGE_NAME}
   * Title - User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""
class replaceString :

    # constructor
    def __init__(self):
        self.userName = " "

    # Method To Accepting and check the min character condition
    def main(self):
        self.userName = input("Enetr the User Name : ")
        lenght = len(self.userName)
        if lenght > 3 :
            print ('Hello '+ self.userName +', How are you?')
        else :
            print('Enter min 3 char')

# Main method
if __name__ == '__main__':

    # Exception Handling
    try :
        stringObject = replaceString()
        stringObject.main()
    except :
        print('Exception Raised.')