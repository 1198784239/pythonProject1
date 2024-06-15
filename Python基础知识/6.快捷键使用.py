#-----------------------------类继承---------------------------------
# class Cat():
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#         print('sdsd')
#     def say_hello(self):
#         print(f'hello,{self.name}')
#     def say_goodbye(self):
#         print(f'goodbye,{self.name}')
#     def say_bye(self):
#         print(f'bye,{self.age}')
# # Cat('李克聪',22).say_hello()
#
# class Dog(Cat):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         print('孩子')
#
# Dog('哇',22).say_goodbye()

#-----------------------------装饰器---------------------------------
def my_decorator(func):
    def inner():
        print('有函数执行了')
        func()
        print('有函数执行完毕了')
    return inner

@my_decorator
def say_hello():
    print('Hello')

say_hello()

# ---------------带参数的装饰器--------------------------
def valid_type_setup(input_type):
    #装饰器
    def decorator(func):
        def inner(*args,**kwargs):
            for i in args:
                if type(i) != input_type:
                    print('请输入类型必须是',input_type)
                    return
                return func(*args,**kwargs)
        return inner
    return decorator

@valid_type_setup(str)
def string(*args):
    for i in args:
        print(i.upper())

string('hello')

def int_process(*args):
    print(sum(args))

int_process(1,2,3)