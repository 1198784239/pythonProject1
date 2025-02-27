
# def Outers(func):
#     def wrapper(*args, **kwargs):
#         print("准备开始打印{}".format(func.__name__))
#         res = func(*args, **kwargs)
#         print("打印结束{}".format(func.__name__))
#         return res
#     return wrapper
# @Outers
# def Inter(a,b):
#     return a+b
#
# # Inter(2,5)
# print(Inter(2,5))

# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def print(self):
#         print(self.name, self.age)
#
# name=Person("李先生",22)
# name.print()

# 带参数装饰器
def Ti(time):
    def Mou(func):
        def wrapper(*args, **kwargs):
            result = []
            for i in range(time):
                res=func(*args, **kwargs)
                result.append(res)
            return result#重要
        return wrapper
    return Mou
@Ti(5)
def num(a,b):
    return a*b

print(num(2,3))

class Anmails():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name)

class Dog(Anmails):
    def speak(self):
        print(self.name)

Dog("旺财").speak()


class Person():
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def move(self):
        print(f"{self.name} 向前移动。")

    def attack(self):
        pass

class Warrior(Person):
    def __init__(self,name):
        super().__init__(name,5)

    def attack(self):
        print(f"{self.name} 使用剑进行攻击。")

class Mage(Person):
    def __init__(self,name):
        super().__init__(name,5)

    def attack(self):
        print(f"{self.name} 使用魔法进行攻击。")

class Archer(Person):
    def __init__(self,name):
        super().__init__(name,90)

    def attack(self):
        print(f"{self.name} 使用弓箭进行攻击。")

# 创建不同角色
warrior = Warrior("战士张三")
mage = Mage("法师李四")
archer = Archer("射手王五")

def pefrom_attack(character):
    character.attack()

pefrom_attack(warrior)
pefrom_attack(mage)
pefrom_attack(archer)