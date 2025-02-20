class Decrease:
    def __init__(self, number):
        self.number = number

    def decrease(self):
        while self.number > 0 or self.number == 0:
            print(self.number)
            self.number -= 1


class Score:
    def __init__(self, grade):
        self.grade = grade

    def assess(self):
        if self.grade >= 90:
            print("优秀")
        elif self.grade >= 80:
            print("良好")
        elif self.grade >= 70:
            print("中等")
        elif self.grade >= 60:
            print("及格")
        else:
            print("不及格")


class Lift:
    def __init__(self):
        self.nowfloor = 1

    def floorupdown(self, targetfloor):
        if targetfloor > self.nowfloor:
            self.nowfloor = targetfloor
            print("电梯向上运行")
        elif targetfloor < self.nowfloor:
            self.nowfloor = targetfloor
            print("电梯向下运行")
        else:
            print("到达目标楼层")


while True:
    num = int(input("请选择递减输出1，成绩等级评定2，电梯运行3，退出0 ："))
    if num == 1:
        while True:
            number = int(input("请输入一个整数（输入0退出）："))
            if number == 0:
                break
            decrease = Decrease(number)
            decrease.decrease()
    elif num == 2:
        while True:
            grade = int(input("请输入成绩（输入负数退出） :"))
            if grade < 0:
                break
            assessgrade = Score(grade)
            assessgrade.assess()
    elif num == 3:
        updown = Lift()
        while True:
            targetfloor = int(input("请输入目标楼层（输入0退出）："))
            if targetfloor == 0:
                break
            updown.floorupdown(targetfloor)
    elif num == 0:
        break
