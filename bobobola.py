from pyray import *
import math


class churchil():
    def __init__(self, position : Vector2, width : int, heigth  : int, color = BLACK):
        self.position = position
        self.width = width
        self.heigth = heigth
        self.color = color

    def render(self):
        draw_rectangle(int(self.position.x),int(self.position.y),self.width,self.heigth,self.color)


class pelota():
    def __init__(self, position, radio, speed, color = BLACK):
        self.position = position
        self.radio = radio
        self.speed = speed
        self.color = color
    def render(self):
        draw_circle(self.position.x,self.position.y,self.radio,self.color)
        self.position = self.position+self.speed
        if(self.position.x >= get_screen_width()-self.radio or self.position.x < self.radio):
            self.speed.x = self.speed.x * -1
        if(self.position.y >= get_screen_height()-self.radio or self.position.y < self.radio):
            self.speed.y = self.speed.y * -1

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2(self.x / scalar, self.y / scalar)
        return NotImplemented

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2(self.x / mag, self.y / mag)
        return Vector2(0, 0) 

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

w = 1080
h = 820
init_window(w,h,'holy window')
set_target_fps(80)

bola = pelota(Vector2(int(w/2), int(h/2)), 20, Vector2(3,3))
player1 = churchil(Vector2(10,h/2),5,10)

while not window_should_close():
    clear_background(WHITE)
    player1.render()
    bola.render()
    end_drawing()
