print('inheritance'.upper())
print('')

class robot:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight + 'lbs'
    
class r1(robot):
    pass

class r2(robot):
    pass

robot1 = r1('Jeff', '120')
robot2 = r2('Jerry', '100')

print(robot1.name + ' ' + robot2.weight)


class aircraft:
    #sound = ''
    def __init__(self, name):
        self.name = name
    def engine_start(self):
        print("{}{}{} I am a {}".format(self.sound, self.sound, self.sound,  self.name))
        
class helicopter(aircraft):
    sound = "chuca"
    
Blackhawk = helicopter('Blackhawk')
Blackhawk.engine_start()
class Jet(aircraft):
    sound = "yuuuew"
    
f = Jet("F22")
f.engine_start()
print('')
print('composition'.upper())
print('')

class Repository:
    def __init__(self):
        self.packages = {}
    def add_packages(self, packages):
        self.packages[packages.name] = packages
    def del_packages(self, selected_packages):
        self.packages.pop(selected_packages)
    def sum_packages(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

#bleh = Repository()
#bleh.add_packages({bleh.f})
    
print('')
print('modules'.upper())
print('')

import random
random_between_these_numbers=random.randint(1,10)
print(random_between_these_numbers)

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now + datetime.timedelta(days=28))

        