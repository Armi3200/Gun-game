import turtle
import random



screen = turtle.Screen()
screen.title('Deneme oyunu')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

controller = turtle.Turtle()
controller.speed(0)
controller.shape('square')
controller.color('white')
controller.penup()
controller.goto(0, -120)
controller.shapesize(2, 1)

bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape('triangle')
bullet.color('red')
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.hideturtle()
bullet.goto(0, -120)
bullet.state = 'ready'  



target = turtle.Turtle()
target.speed(0)
target.color('blue')
target.shape('circle')
target.penup()

point = 0

writing = turtle.Turtle()
writing.speed(0)
writing.color('white')
writing.penup()
writing.hideturtle()
writing.goto(0, 200)
writing.write('Point : {}'.format(point), align="center")



def go_right():
    x = controller.xcor()
    x = x + 15
    controller.setx(x)
def go_left():
    x = controller.xcor()
    x = x - 15
    controller.setx(x)
def fire_bullet():
    if bullet.state == 'ready':
        bullet.state = 'fire'
        x = controller.xcor()
        y = controller.ycor() + 10  
        bullet.goto(x, y)
        bullet.showturtle()



screen.listen()
screen.onkeypress(go_right, 'Right')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(fire_bullet, 'space')


while True:
    screen.update()
    if controller.xcor()>240 or controller.xcor()<-240:
       controller.goto(0, -120)

       point = 0
       writing.clear()
       writing.write('Point : {}'.format(point), align="center")
 
    
    # Mermiyi hareket ettirme
    if bullet.state == 'fire':
        y = bullet.ycor()
        y += 10  # Mermi hızı
        bullet.sety(y)
    
    # Hedefle çarpışma kontrolü
    if bullet.distance(target) < 20:  # Mermi ve hedef arasındaki mesafeyi kontrol ediyoruz
        bullet.hideturtle()
        bullet.state = 'ready'
        point += 1
        writing.clear()
        writing.write('Point : {}'.format(point), align="center")
        target.goto(random.randint(-240, 240), random.randint(100, 200))  # Yeni bir hedef konumu belirle

    # Mermi ekran dışına çıktığında sıfırlama
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet.state = 'ready'