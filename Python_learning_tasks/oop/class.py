# A Class is a blueprint for creating objects.

# Example of a class instance could be class Car 
# and the object could be BMW.

# Examples of writing classes

# Class declared
class Person:
    # Class attributes/variables
    name = ''

    # Class initializer/constructor
    def __init__(self):
        # Object attributes/variables
        self.name = ''
        self.age = 0
        self.nationality = ''

    # Methods declared
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old. My nationality is {self.nationality}.'
    
    # Create destructor method
    def __del__(self):
        print('{} {} : Destructor Invoked'.format(self.name, self.age))
    
def main():
    # person1 & person2 are objects
    person1 = Person()
    print(person1.greet())
    # print(person2.greet())

    # Values
    person1.name = 'Jane Doe'
    person1.age = 35
    person1.nationality = 'British'

    # Accessing person1 attributes
    print(' Person 1 details '.center(25, '-'))
    print('Name: {}'.format(person1.name))
    print('Age: {}'.format(person1.age))
    print('Nationality: {}'.format(person1.nationality))

    # Accessing person2 attributes 

    # Class attributes
    print(' Class attributes '.center(25, '-'))
    print('person1:', person1.name)

    # Delete
    print('Deleting Objects'.center(25, '-'))
    del person1
    
# this statement will be used to consume the class and make more objects
if __name__ == '__main__':
    main()