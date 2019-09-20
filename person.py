class Person(object):
    def __init__(self,person_name):
        self.name = person_name    
        pass
    def say_hello(self):
        print("Hi! everyone! My name is {}!".format(self.name))

Franklin = Person("Beck")
Franklin.say_hello()
 

