"""
   * author - ${Suraj Jadhav}
   * date - ${24-Nov-20}
   * time - ${10:00 AM}
   * package - ${PACKAGE_NAME}
   * Title - Write a program WindChill that takes two double command-line arguments t and v and prints the wind chill.
             Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather
             Service defines the effective temperature (the wind chill)
"""
class windChill :

    # constructor
    def __init__(self) :
        self.temperature = 0
        self.velocity = 0
        self.windChill = 0

    # Accept Value in range
    def acceptingValue(self) :
        flag = True
        # Accept Temperature
        while (flag) :
            self.temperature = float(input('Enter Temperature in Fahrenheit ragne (less than 50) : '))
            if self.temperature < 50 :
                flag = False
                print(f'Enter Temperature in rage = {self.temperature}')
            else :
                print(f'Enter Temperature = {self.temperature}\nnot in range  \nEnter again ragne (less than 50).')
        flag = True
        # Accept Velocity
        while (flag):
            self.velocity = float(input('Enter Velocity in miles per hour ragne (greter than 3 and less than 120) : '))
            if 3 < self.velocity < 120:
                flag = False
                print(f'Enter Velocity in rage = {self.velocity}')
            else:
                print(f'Enter Velocity = {self.velocity}\nnot in range  \nEnter again ragne (greter than 3 and less than 120).')

    # Calculate Wind chill
    def calculatewindChill(self) :
        self.windChill = 35.74 + (0.6215 * self.temperature) + (((0.4275 * self.temperature) - 35.75) * pow(self.velocity, 0.16))
        print('effective temperature : ',self.windChill)


# main
if __name__ == '__main__' :
    # Exception Handling
    try :
        # creating object
        windChillobject = windChill()
        # Calling Method AcceptingValue
        windChillobject.acceptingValue()
        # Calling Method CalculatewindChill
        windChillobject.calculatewindChill()
    except :
        print('Exception Raised.')