

class Person():
    
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        print('Person is created')
        
    def who_am_i(self):
        print('I am a person')
        
    def eat(self):
        print('I am eating')


class Student(Person):
    
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.student_number = number
        print('Student is created')
    #overriding    
    def who_am_i(self):
        print('I am a student') 

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #this is the alternative of above (Person.__init__(self, fname, lname))   
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
    
p1 = Person('furkan','kurt')
s1 = Student('emine','ekici', 55)
t1 = Teacher('sude', 'kurt', 'math')

print(p1.first_name + ' '+ p1.last_name)
print(s1.first_name + ' '+ s1.last_name + ' '+ str(s1.student_number))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
