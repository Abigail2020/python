"""
@Time:  2021/2/19
@Author:chenzhe

"""
from python.python_oop.homework.animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.age = "1"

    def catch_mouse(self):
        print("猫会捉老鼠～")

    def shout(self):
        print("喵喵叫")


if __name__ == "__main__":
    cat = Cat()
    print(cat.age)
    cat.shout()
    cat.catch_mouse()
