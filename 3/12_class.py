# class는 class 클래스이름() 로 정의함
# 들여쓰기에 따라 속성과 메서드가 정의됨.
# self > 한 클래스의 모든 메서드는 인스턴스화된 클래스 객체 사본을 첫번째 파라미터로 받음
class MyClass():
    def some_method(self):
        print(f"Say hi to {self}")

myObject = MyClass()

myObject.some_method()

# 모든 클래스는 __init__ 메서드를 가짐
# 클래스가 인스턴스화되면 해당 메서드 호출
# 만약 미정의시 파이썬 기본객체클래스에서 상속된 기본 메서드 사용
MyClass.__init__

# 일반적으로 __init__메서드에서 객체 속성 정의
class MyOtherClass():
    def __init__(self, name):
        self.name = name

MyOtherObject = MyOtherClass('Sammy')

MyOtherObject.name