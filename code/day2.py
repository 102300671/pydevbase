class Day2:
    def __init__(self, result, my_name, my_age, my_sex):
        self.result = result
        self.my_name = my_name
        self.my_age = my_age
        self.my_sex = my_sex

    def one(self):
        print(self.result)

    def two(self):
        print(f"我叫{self.my_name}，今年{self.my_age}岁，性别是{self.my_sex}")

    def three(self):
        print("i=666是int\nf=123.456是float\nb1=True，b2=False和b3=1>2是bool")

    def four(self):
        print("关关雎鸠，在河之洲，窈窕淑女，君子好逑，\n参差荇菜，左右流之，窈窕淑女，寤寐求之。")

    def five(self):
        x = 10
        y = 5
        bool1 = x > y
        print(bool1)


day2 = Day2(30 - 15, "吕林涵", 19, "男")
for _ in range(0, 5):
    no = int(input("请输入作业编号:1,2,3,4,5:"))
    if no == 1:
        day2.one()
    elif no == 2:
        day2.two()
    elif no == 3:
        day2.three()
    elif no == 4:
        day2.four()
    else:
        day2.five()
