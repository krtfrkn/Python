#class
class Person:
    
    #class attributes
    address='no info'
    
    #constructor()
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.year = year
        print('init method is working')
    #instancce methods
    def intro(self):
        print('hello this is instance method from class '+ self.name)
    def calculate_age(self):
        return 2023 - self.year

#object (instance)
p1 = Person('furkan',1986)
p2 = Person(year=1988, name='emine')

print(f'p1 name:{p1.name} year:{p1.year} address:{p1.address}')
print(f'p2 name:{p2.name} year:{p2.year} address:{p2.address}')

print(p1.intro())
print(p2.intro())
print(p1.calculate_age())
print(p2.calculate_age())

class Circle:
    # Class object attribute
    pi = 3.14
    
    def __init__(self, radius=1): #it means radius is 1 as default
        self.radius = radius
        
    #Methods
    def calculating_circumference(self):
        return 2 * self.pi * self.radius
    
    def calculating_area(self):
        return self.pi * (self.radius**2)

c1 = Circle() #radius=1
c2 = Circle(5)

print(f'c1 : area = {c1.calculating_area()} circumference = {c1.calculating_circumference()}')
print(f'c2 : area = {c2.calculating_area()} circumference = {c2.calculating_circumference()}')
 