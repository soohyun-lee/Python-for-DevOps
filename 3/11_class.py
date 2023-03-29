class MyClass():
    def some_method(self):
        print(f"Say hi to {self}")

myObject = MyClass()

myObject.some_method()

MyClass.__init__

class MyOtherClass():
    def __init__(self, name):
        self.name = name

MyOtherObject = MyOtherClass('Sammy')

MyOtherObject.name