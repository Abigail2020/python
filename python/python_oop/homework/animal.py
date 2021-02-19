"""
@Time:  2021/2/19
@Author:chenzhe

"""


class Animal:

    def __init__(self):
        self.name = "animal"
        self.color = "color"
        self.age = "age"
        self.gender = "gender"

    def shout(self):
        print("动物叫")

    def run(self):
        print("动物跑")


if __name__ == "__main__":
    animal = Animal()
    animal.shout()
