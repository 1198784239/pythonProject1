
def Paymon(ored):
    def Password():
        password = input('请输入密码')
        if password == '123456':
            ored()
            # print('购买成功')
        else:
            print('密码错误')

    return Password


@Paymon
def buy():
    print('买入成功')

@Paymon
def Sale():
    print('卖出成功')


buy()
Sale()