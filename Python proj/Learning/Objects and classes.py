class PartyAnimal:
    x=0
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
    
    
    def party(self):
        self.x=self.x+1
        print('my name is {} and imma  {}... x is now = {}'.format(self.name, self.typ, self.x))
        
Giraff = PartyAnimal('Harold', 'Giraff')


Giraff.party()
Giraff.party()
Giraff.party()
Giraff.party()



class Robot:
    y=0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'is CONSTURCTED')
        
    def increase(self):
        self.y += 1
        print(self.name,' is: ',self.y)
        
    def __del__(self):
        print('I AM DECONSTRUCTED AT ', self.y)
        
R1 = Robot('Fred')
R2 = Robot('Leonardo')
R1.increase()
R1.increase()
R2.increase()

class FootballFan(Robot):
    points = 0
    def touchdown(self):       
        self.increase()
        extra_point = input('Extra Point made? y or n?')
        if extra_point == 'y':
            self.points += 7
        elif extra_point == 'n':
            self.points += 6
        print(self.name, ' made ', self.points, ' points')
Rodger = FootballFan('Rodger')
Rodger.touchdown()
        

