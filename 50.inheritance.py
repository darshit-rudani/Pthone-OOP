class Person( object ):
        def __init__(self,name,age):
                self.name = name
                self.age = age
        def display(self):
                print(self.name)
                print(self.age)

class Person2(Person):
        def __init__(self,name,age,salary,post):
                self.salary = salary
                self.post = post
                Person.__init__(self,name,age)
        def display2(self):
                print(self.salary)
                print(self.post)

a = Person2('Darshit',20,50000,"It")
a.display()
a.display2()

