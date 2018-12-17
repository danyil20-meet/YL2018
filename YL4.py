"""
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def Area(self):
        return self.width * self.height
        
    def Perimeter(self):
        return (self.width + self.height) * 2
    

rec1 = Rectangle(3, 4)
print(rec1.Area())
print(rec1.Perimeter())


class Person(object):
    def __init__(self, name, age, city, gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
    def eat(self, food):
        print(self.name + " has eaten " + food)
    def sleep(self, hours):
        print(self.name + " has slept for " + (str)(hours))

p1 = Person("Bob", 16, "New York", "male")
p1.eat("ice cream")
p1.sleep(5)
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        string = ""
        for i in range(len(self.lyrics)):
            if (self.lyrics[i] == ","):
                print(string)
                string = ""
            else:
                string += self.lyrics[i]

s1 = Song("Hey there brother watch your little lady,Shes a little faster than you think,Hey there brother watch your little lady, Shell be sneaking round every time you blink")
s1.sing_me_a_song()
