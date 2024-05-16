class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Name(self):
        print(self.name)
    def Age(self):
        print(self.age)

Cat('小李',30).Name()

# -----------------------------继承-----------------------------
class Father():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def PrintInfo(self):
        print("我的名字是:"+self.name, "今年:",self.age)

class Son():
    def __init__(self, name,age):
        super().__init__(name, age)
father =Father('sds',54)
father.PrintInfo()