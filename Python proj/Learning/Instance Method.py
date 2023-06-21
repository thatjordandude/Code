#class Pigman: #method happen on single instance of a class
#    def speak(self): #define the method
#        print('oink oink')
#Hamlet = Pigman()
#Hamlet.speak()

print('___________')

class Pigman:
#    name = 'Steve'
    def speak(self): 
        print("oink oink! I'm {}! master of all".format(self.name))
    years = 0
    def pig_years(self):
        return (self.years * 18)
hamlet = Pigman()
hamlet.name = 'Hamlet'
hamlet.speak()
hamlet.years = 2
print(hamlet.pig_years())
parrywinkle = Pigman()
parrywinkle.name = "Parrwinkle"
parrywinkle.speak()
parrywinkle.years = 3
print(parrywinkle.pig_years())
print('\n')

print('\n')
print('following is contructor and other special methods')
print('')

class Apple:
    #this is this constructor(__init__)
    def __init__(self, color, flavor):
        #you need (self) everything else is
        #defining what an apple is
        self.color = color
        self.flavor = flavor
        
    def __str__(self):
        return 'This apple is {} and its flavor is {}'.format(self.color, self.flavor)
      #the above allows for you to print just the object with predefiined variables
honeycrisp = Apple('red', 'sweet')
print(honeycrisp.color)
print(honeycrisp)

print('')

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return 'hi, my name is ' + self.name 

# Create a new instance with a name of your choice
some_person = Person('Brad')  
# Call the greeting method
print(some_person.greeting())
print('')
print('Documenting Functions, Classes, and Methods'.upper())

#print(help(Apple))
def example_of_doc_string(x):
    """this is an example of a docs string"""
    return x
print(help(example_of_doc_string))

print('')
