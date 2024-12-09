# Examples of getter and setter properties
# which can be used with the following functions to get and set

# Declaring the Class constructor
class Person:
    # Initializes a new instance of the Person class
    def __init__(self):
        self._name = ''
        self._age = 0
        self._nationality = ''

    # declare setter method through @property 
    # using properties is much more efficient and works as if its a variable
    # but these are methods inside the class declaration
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('Age must be a non-negative integer.')
        
    @property
    def nationality(self):
        return self._nationality
    
    @nationality.setter
    def nationality(self, value):
        if isinstance(value, str):
            self._nationality = value
        else:
            raise ValueError('Nationality must be a string.')