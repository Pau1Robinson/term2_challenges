'''
Answer for challenge 23-8 part2
'''

class Dog:
    '''
    Class to track the various characteristics of a dog
    '''

    def __init__(self, dog_name, dog_age, dog_location, dog_walks, dog_walks_distance):
        '''
        A _dunder_ method, which runs when a new object is instantiated from this class. When creating this object it must be passed a dog_name string and a dog_age int.
        '''
        self.dog_name = dog_name
        self.dog_age = dog_age
        self.dog_location = dog_location
        self.dog_walks = dog_walks
        self.dog_walks_distance = dog_walks_distance
        print("I've been initialized!")

    def speak(self):
        '''
        Prints the dogs name and age.
        '''
        print(f'{self.dog_name} says woof! I am {self.dog_age} years old! I am in {self.dog_location}')

    def walk(self, dog_location, distance):
        '''
        Updates the number of walks the dog has been on
        '''
        self.dog_walks += 1
        self.dog_walks_distance = self.dog_walks_distance + distance

    def display_walks(self):
        '''
        Displays the number of walks the dog has been on
        '''
        print(f'I have been on {self.dog_walks} walks in {self.dog_location} for {self.dog_walks_distance}m today')

doggo = Dog('Rover', 2, 'Sydney', 0, 0)
doggo.walk('sydney', 200)
doggo.speak()
doggo.display_walks()

doggo = Dog('Lassie', 5, 'melbourne', 0, 0)
doggo.walk('melbourne', 100)
doggo.walk('melbourne', 200)
doggo.speak()
doggo.display_walks()