import random

class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.teacher = teacher

    def study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.teacher.teach()

    def sleep(self):
        print("I will sleep")
        self.gladness += 3

    def chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress = 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        return self.alive

    def end_of_day(self, day):
        print(f"{'='*20} Day {day} {'='*20}")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self):
        day = 1
        while day <= 365 and self.alive:
            print(f"{'='*20} Day {day} {'='*20}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.study()
            elif live_cube == 2:
                self.sleep()
            elif live_cube == 3:
                self.chill()
            self.end_of_day(day)
            self.is_alive()
            day += 1
        if day > 365:
            print("One year has passed.")


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print("Teaching the student.")


teacher = Teacher("Professor Snape")
student = Student("Harry Potter", teacher)
student.live()
