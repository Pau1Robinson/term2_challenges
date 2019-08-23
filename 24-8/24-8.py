'''
Answer for 24-8 challenges part 1
'''

class vehicle:
    '''
    Define the characteristics of a vehicle
    '''
    def __init__(self, model, manufacturer, fuel):
        self.model = model
        self.manufacturer = manufacturer
        self.fuel = int(fuel)

    def refuel(self):
        '''
        Asks for an amount of fuel to add then adds that to fuel
        '''
        fuel_input = input('how much fuel do you want to put in?\n')
        self.fuel += int(fuel_input)
        print(f'{fuel_input}Ls of fuel have been put in {self.manufacturer} {self.model}')

    def fuel_level(self):
        '''
        Prints the current amount of fuel in the vehicle
        '''
        print(f'there is {self.fuel}Ls of fuel in {self.manufacturer} {self.model}')

class car(vehicle):
    '''
    Defines the characteristics of a car
    '''
    def __init__(self, model, manufacturer, fuel, windows):
        super().__init__(model, manufacturer, fuel)
        self.windows = windows

    def wind_up_windows(self):
        '''
        If the winds are down winds the windows up and updates windows
        '''
        if self.windows is True:
            print(f'Winding up the windows of {self.manufacturer} {self.model}')
            self.windows = False
        elif self.windows is False:
            print(f'The winds of {self.manufacturer} {self.model} are already up')

class low_rider(vehicle):
    '''
    Defines the characteristics of a low_rider
    '''
    def __init__(self, model, manufacturer, fuel):
        super().__init__(model, manufacturer, fuel)

    def wheelie(self):
        if self.fuel > 0:
            print(f'{self.manufacturer} {self.model} did a wheelie')
        else:
            print(f'{self.manufacturer} {self.model} does not have enough fuel to do a wheelie')

Civic = car('civic', 'honda', 10, True)
Civic.refuel()
Civic.fuel_level()
Civic.wind_up_windows()
Civic.wind_up_windows()

low_rider = low_rider('Harley Davidson', 'low rider', 0)
low_rider.wheelie()
low_rider.refuel()
low_rider.fuel_level()
low_rider.wheelie()
