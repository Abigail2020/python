"""
@Time:  2021/2/19
@Author:chenzhe

自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】

"""


# 父类/基类/超类 可以被子类继承
class Animal:

    # 构造方法，在类实例化时自动执行 
    def __init__(self, name, color, age, gender):
        # 实例变量，方法之中，以self.命名，相当于类的全局变量
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print("动物叫")

    # 私有方法
    @staticmethod
    def __run():
        print("动物跑")


if __name__ == "__main__":
    animal = Animal("maomi", "white", "1", "female")
    print(animal.age)
    animal.shout()
    # 私有方法不能被实例化
    # animal.__run()
