from pyray import *
import math
import gc
import time


class Churchil():
    def __init__(self, position : Vector2, width : int, heigth  : int, color = WHITE):
        self.position = position
        self.width = width
        self.heigth = heigth
        self.color = color

    def render(self):
        draw_rectangle(int(self.position.x),int(self.position.y),self.width,self.heigth,self.color)


class Player(Churchil):
    def __init__(self, position : Vector2, width : int, heigth  : int, speed : Vector2, upBtn : KeyboardKey, downBtn: KeyboardKey,  color = WHITE):
         super().__init__(position, width, heigth, color)
         self.speed = speed
         self.upBtn = upBtn
         self.downBtn = downBtn
         self.puntos = 0
    def move(self):
        if is_key_down(self.upBtn):
            self.position.y = self.position.y - self.speed.y
        if is_key_down(self.downBtn):
            self.position.y = self.position.y + self.speed.y
        """if is_key_down(KeyboardKey.KEY_A): # This two are for debugging
            self.position.x = self.position.x - self.speed.x
        if is_key_down(KeyboardKey.KEY_D):
            self.position.x = self.position.x + self.speed.x"""


class Pelota():
    def __init__(self, position : Vector2, radio : int, speed : Vector2, color = WHITE):
        self.position = position
        self.radio = radio
        self.speed = speed
        self.color = color
    def render(self):
        draw_circle(self.position.x,self.position.y,self.radio,self.color)
        self.position = self.position+self.speed

        if(self.position.x >= get_screen_width()-self.radio or self.position.x < self.radio):
            self.speed.x = self.speed.x * -1
            if self.position.x >= get_screen_width()-self.radio :
                return "Right"
            else:
                return 'Left'

        if(self.position.y >= get_screen_height()-self.radio or self.position.y < self.radio):
            self.speed.y = self.speed.y * -1

        for player in [i for i in gc.get_objects() if isinstance(i, Player)]:
            if((self.position.x - self.radio <= player.position.x + player.width and self.position.x + self.radio >= player.position.x) and (self.position.y - self.radio <= player.position.y + player.heigth and self.position.y + self.radio >= player.position.y)):
                #print(f"Collision at {time.time()}") # Debug
                if self.position.x > player.position.x and self.position.x < player.position.x + player.width:
                    self.speed.y = self.speed.y * -1
                elif self.position.y > player.position.y and self.position.y < player.position.y + player.heigth:
                    self.speed.x = self.speed.x * -1
                else:
                    self.speed.x *= -1
                    if (player.position.y + (player.heigth / 2) < self.position.y):
                        self.speed.y = abs(self.speed.y)
                    elif (player.position.y + (player.heigth / 2) > self.position.y):
                        self.speed.y = -abs(self.speed.y)


    def collisionc(self,collider : Churchil):
        if self.position.y + self.radio >= collider.position.y and self.position.y - self.radio <= collider.position.y+collider.heigth and self.position.x + self.radio >= collider.position.x and self.position.x - self.radio <= collider.position.x:    
            return True
        else: return False
    

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, m):
        if isinstance(m, (int, float)):
            return Vector2(self.x * m, self.y * m)
        elif isinstance(m, Vector2):
            return Vector2(self.x * m.x, self.y * m.y)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2(self.x / mag, self.y / mag)
        return Vector2(0, 0) 
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def round(self):
        return Vector2(round(self.x), round(self.y))

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
    

w,h = 1080,800

init_window(w,h,'holy window')
set_target_fps(60)

bola = Pelota(Vector2(int(w/2), int(h/2)), 20, Vector2(2,2))
player0 = Player(Vector2(10,h/2),10,70,Vector2(5,5), KeyboardKey.KEY_UP, KeyboardKey.KEY_DOWN)
player1 = Player(Vector2(1060,h/2),10,70,Vector2(5,5), KeyboardKey.KEY_W, KeyboardKey.KEY_S)

while not window_should_close():
    clear_background(BLACK)
    player0.render()
    player0.move()
    player1.render()
    player1.move()
    bola.render()
    match bola.render():
        case 'Right':
            player0.puntos+=1
        case 'Left':
            player1.puntos+=1
        case _:
            pass
    draw_text(str(player0.puntos),w-1050, 10, 20, RED)
    draw_text(str(player1.puntos),w-50, 10, 20, RED)

    end_drawing()