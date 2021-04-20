class Car:
    """base class for car"""

    def __init__(self, make, speed, max_speed, gear):
        self.make = make
        self.speed = 10
        self.max_speed = 169
        self.gear = 5

    def set_make(self, make):
        self.make = make

    def set_speed(self, speed):
        self.speed = 10


    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed

    #methods
  

    def accelerate(self):
        self.speed +=5

    def brake(self):
        self.speed -=5


   