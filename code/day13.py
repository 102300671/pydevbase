class Student:
    def __init__(self,name,age,grades,avegrade):
        self.name = name
        self.age = age
        self.grades = grades
        self.avegrade = avegrade
    def average_grade(self):
        self.avegrade = sum(self.grades)/len(self.grades)
    def display_info(self):
        print(f"姓名:{self.name},年龄:{self.age},平均成绩:{self.avegrade}")


class GraduateStudent(Student):
    def __init__(self,name,age,grades,avegrade,thesis_topic):
        super().__init__(name,age,grades,avegrade)
        self.thesis_topic = thesis_topic
    def display_info(self):
        print(f"姓名:{self.name},年龄:{self.age},平均成绩:{self.avegrade},论文题目:{self.thesis_topic}")


    name=input("请输入姓名:")
    age=input("请输入年龄:")
    grades = []
    for i in range(3):
        grade = int(input("请输入成绩:"))
        grades.append(grade)
    thesis_topic = input("请输入论文题目:")
    student = GraduateStudent(name,age,grades,0,thesis_topic)
    student.average_grade()
    student.display_info()