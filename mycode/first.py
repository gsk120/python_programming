"""
파이썬 모듈 안에는 함수와 클래스를 선언 할 수 있다
block comment ("세개)
line comment (#)
"""

# 함수와 람다 실습
def add(n1,n2):
    #pass
    return n1+n2
print(add(1,2))
print(type(add))

add2 = lambda n1,n2: n1+n2
print(add2(100,200))
print(type(add2))

# class 선언
class User:
    # pass
    def __init__(self, name):
        self.name = name
    # self는 자기 자신 this와 동일

    # to string 함수 재정의 (overriding)
    def __str__(self):
        return self.name

# class 객체 생성
user = User("파이썬")
print(user)