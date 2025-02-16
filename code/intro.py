class Intro:
  def __init__(self,name,age, hometown,food):
    self.name=name
    self.age=age
    self.hometown=hometown
    self.food=food
  def intro(self):
    print(f"我的名字是{self.name},今年{self.age}岁，我来自{self.hometown},我喜欢的美食是{self.food}")
self_intro=Intro("吕林涵",19,"山西","兰州牛肉拉面")
self_intro.intro()
name=input("姓名:")
age=int(input("年龄:"))
hometown=input("家乡:")
food=input("喜欢的美食:")
your_intro=Intro(name,age,hometown,food)
your_intro.intro()