class Day3:
  @staticmethod
  def one():
    print("C")
  @staticmethod
  def two():
    print("D")
  @staticmethod
  def three():
    print("A")
  @staticmethod
  def four():
    print("D")
  @staticmethod
  def five():
    name,age=input("请输入姓名 年龄：").split()
    print(f"姓名：{name}，年龄：{int(age)+10}")
  @staticmethod
  def six(n):
    a=2
    b=3
    print(a,b)
    if n==1:
      a,b=b,a
    elif n==2:
      t=a
      a=b
      b=t
    print(a,b)
  @staticmethod
  def seven(n):
    if n%2==0:
      print(f"{n}是偶数")
    else:
      print(f"{n}是奇数")
  @staticmethod
  def eight():
    res=3>4 and not 4>3 or 1==3 and 'x'=='x' or 3>3
    print(res)


for _ in range(0,8):
  day3=Day3
  num=int(input("请输入作业编号(1,2,3,4,5,6,7,8):"))
  if num==1:
    day3.one()
  elif num==2:
    day3.two()
  elif num==3:
    day3.three()
  elif num==4:
    day3.four()
  elif num==5:
    day3.five()
  elif num==6:
    for _ in range(0,2):
      n=int(input("请输入方式编号(1,2):"))
      day3.six(n)
  elif num==7:
    while True:
      n=int(input("请输入一个整数，输入0退出:"))
      if n==0:
        break
      day3.seven(n)
  else:
    day3.eight()