import tkinter as tk
from tkinter import simpledialog

"""
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
"""

"""
year = simpledialog.askinteger("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

if year <= 1900:
    print ('Woah, that is the past!')
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
"""

"""
class Person:
  def __init__(self, first, last):
    self.first = first
    self.last = last
  def speak(self):
      print("My name is " + self.first + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
"""

"""
exam_one = simpledialog.askinteger("Input", "Input exam grade one: ", parent=tk.Tk().withdraw())

exam_two = simpledialog.askinteger("Input" , "Input exam grade two: ", parent=tk.Tk().withdraw())

exam_3 = simpledialog.askinteger("Input" , "Input exam grade three: ", parent=tk.Tk().withdraw())

#print((str)(exam_one) + " " + (str)(exam_two) + " " + (str)(exam_3))
grades = [exam_one, exam_two, exam_3]
sum = 0


for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
"""

"""
class Person:
   def __init__(self, name, fav_food, age, color):
       self.name = name
       self.fav_food = fav_food
       self.age = age
       self.color = color
        

   def define_color(self, color="Red"):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16, "Green")
a.define_color("Black")
a.print_info()

b = Person("Jake", "Burger", 15, "Purple")
b.print_info()
"""

"""
class Bear():
    def __init__(self, name):
                self.name = name
                print("A new bear created. Its name is: " + self.name)
    
    def say_hi(self):
        print("Hi! I’m a bear. My name is " + self.name)
my_bear = Bear("Danny")
my_bear.say_hi()
"""

"""
class Cake():
	def __init__(self, flavor):
		self.flavor = flavor

	def eat(self):
		print("Yummy!!! Eating a " + self.flavor + " cake :)")

cake = Cake("chocolate")
cake.eat()
"""

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1
        if self.age >= 100:
            print("Dong dong, the cat is dead!")
        else:
            print(self.name + " has his " + (str)(self.age) + " birthday!")

my_cat = Cat("Salem", 5)
my_cat.birthday()



