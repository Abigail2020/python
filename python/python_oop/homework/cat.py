"""
@Time:  2021/2/19
@Author:chenzhe

"""
from python.python_oop.homework.animal import Animal


# 子类
class Cat(Animal):
    def __init__(self):
        super().__init__("tom", "yellow", "2", "male")
        self.age = "1"

    def catch_mouse(self):
        print("猫会捉老鼠～")

    def shout(self):
        print("喵喵叫")


if __name__ == "__main__":
    cat = Cat()
    print(cat.age)
    print(cat.name)
    cat.shout()
    cat.catch_mouse()
