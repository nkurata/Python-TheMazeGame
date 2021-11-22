#maze game
#methodes by TokyoEdtech
import turtle
import math
import random

win=turtle.Screen()
win.bgcolor("black") 
win.title("Maze Game")
win.setup(700,700)
win.tracer(0)


#register shapes
images=["playerR.gif","playerL.gif","coin.gif","stone.gif", "enemyR.gif","enemyL.gif","finish.gif"]
for image in images:
    turtle.register_shape(image)

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("playerR.gif")
        self.color("red")
        self.penup()
        self.speed(0) 
        self.gold=0

    def go_up(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()+24
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x=self.xcor()
        move_to_y=self.ycor()-24
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x=self.xcor()-24
        move_to_y=self.ycor()
        self.shape("playerL.gif")
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        self.shape("playerR.gif")
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False

#crete treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("coin.gif")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y) 

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Finish(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("finish.gif")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.goto(x, y)
    
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemyR.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="left":
            dx=-24
            dy=0
            self.shape("enemyL.gif")
        elif self.direction=="right":
            dx=24
            dy=0
            self.shape("enemyR.gif")
        else:
            dx=0
            dx=0
        
        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"
            elif player.xcor()>self.xcor():
                self.direction="right"
            elif player.ycor()<self.ycor():
                self.direction="down"
            elif player.ycor()>self.ycor():
                self.direction="up"

        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy

        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        else:
            self.direction=random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100,200))

    def is_close(self, other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#create levels list
levels=[""]

#define first level
level_1= [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXXT       XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXXT X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX EXXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XXE  XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX           XXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
treasures=[] #treasures
enemies=[] #enemies
finishline=[] #finish
levels.append(level_1)#adds level_1 to levels(list)

def setup_maze(level): #Create level setup fonction
    for y in range(len(level)):
        for x in range(len(level[y])):#get the character at each x,y coordinate + Note the order of y and x in the next line
            character=level[y][x] #calculate the screen x, y coordinates
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character=="X": #check if it is a wall
                pen.goto(screen_x, screen_y)
                pen.shape("stone.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character=="P":
                player.goto(screen_x, screen_y)
            if character=="T":
                treasures.append(Treasure(screen_x, screen_y))
            if character=="E":
                enemies.append(Enemy(screen_x, screen_y))
            if character=="Y":
                finishline.append(Finish(screen_x, screen_y))

            
#instances
pen=Pen()
player=Player()
#walls
walls=[]
#maze setup
setup_maze(levels[1])
#keyboard bindings
turtle.listen() 
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_up,"Up")

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True: #Main Game Loop
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold #add gold to player's gold
            print("Player Gold {}".format(player.gold))
            treasure.destroy() #destroy treasure when aquired
            treasures.remove(treasure) #remove the treasure from treasure list
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Dies!")
    for finish in finishline:
        if player.is_collision(finish):
            if player.gold==200:
                print("Game Won!")
            else:
                print("Get more Gold!")
    win.update()


turtle.Screen().exitonclick()