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

    # Accept Value in range
    def acceptingValue(self):
        # Accept Temperature
        while True:
            temperature = float(input('Enter Temperature in Fahrenheit ragne (less than 50) : '))
            if temperature < 50:
                print(f'Enter Temperature in rage = {temperature}')
                break
            else:
                print(f'Enter Temperature = {temperature}\nnot in range  \nEnter again ragne (less than 50).')
        # Accept Velocity
        while True:
            velocity = float(input('Enter Velocity in miles per hour ragne (greter than 3 and less than 120) : '))
            if 3 < velocity < 120:
                print(f'Enter Velocity in rage = {velocity}')
                break
            else:
                print(f'Enter Velocity = {velocity}\nnot in range  \nEnter again ragne (greter than 3 and less than 120).')
        return temperature, velocity

    # Calculate Wind chill
    def calculatewindChill(self, temperature, velocity):
        windChill = 35.74 + (0.6215 * temperature) + (((0.4275 * temperature) - 35.75) * pow(velocity, 0.16))
        print('effective temperature : ', windChill)


# main
if __name__ == '__main__' :
    while True:
        # Exception Handling
        try:
            # creating object
            windChillobject = windChill()
            # Calling Method AcceptingValue
            temperature, velocity = windChillobject.acceptingValue()
            # Calling Method CalculatewindChill
            windChillobject.calculatewindChill(temperature, velocity)
            break
        except ValueError:
            print('You enter str must enter int value')