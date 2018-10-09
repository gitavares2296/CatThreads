#importing lib for interface grafic
import turtle
#importing lib for treads
import threading


#create a new display to start drawing
def create_screen():
    window = turtle.Screen()
    window.bgcolor("pink")
    return window


#get a new instance of cursor
def get_turtle():
    brad = turtle.Turtle()
    #set properties about cursor
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(4)
    brad.pensize(2)
    return brad


#draw a line using position, distance and angle
def draw(brad,position,distance,angle):
    if(position == 'left'):
        brad.left(angle)
        brad.backward(distance)
    else:
        brad.right(angle)
        brad.forward(distance)


#draw a line using position, distance and angle
def draw_reverse(brad,position,distance,angle):
    if(position == 'left'):
        brad.right(angle)
        brad.backward(distance)
    else:
        brad.left(angle)
        brad.forward(distance)


#call commands of draw to make some lines
def draw_external_lines(brad,position):
    draw(brad,position,50,0)
    draw_reverse(brad,position,90,30)
    draw(brad,position,210,130)
    draw(brad,position,70,45)
    draw(brad,position,36,20)
    brad.hideturtle()


#call commands of draw to make some lines
def draw_shape(brad,position):
    draw(brad,position,50,0)
    draw(brad,position,85,45)
    draw(brad,position,90,115)
    draw(brad,position,30,20)
    draw(brad,position,30,180)
    draw(brad,position,30,60)
    draw_reverse(brad,position,90,99)
    draw(brad,position,150,155)
    draw(brad,position,48,80)
    if(position == 'right'):
        brad.left(106)
        brad.forward(30)
    brad.hideturtle()


#call commands of draw to make some lines
def draw_expression_lines(brad,position):
    draw(brad,position,50,0)
    draw(brad,position,58,150)
    draw(brad,position,58,180)
    draw(brad,position,160,135)
    draw_reverse(brad,position,50,155)
    draw_reverse(brad,position,50,180)
    draw(brad,position,10,50)
    draw(brad,position,10,180)
    draw(brad,position,20,115)
    if(position == 'left'):
        brad.right(27)
        brad.backward(10)
    brad.hideturtle()

#start all threads with a cursor and position
def start_threads(turtles):
    t1 = threading.Thread(target=draw_external_lines,args=(turtles[0],'left',))
    t1.start()
    t2 = threading.Thread(target=draw_external_lines,args=(turtles[1],'right',))
    t2.start()
    t3 = threading.Thread(target=draw_shape,args=(turtles[2],'left',))
    t3.start()
    t4 = threading.Thread(target=draw_shape,args=(turtles[3],'right',))
    t4.start()
    t5 = threading.Thread(target=draw_expression_lines,args=(turtles[4],'left',))
    t5.start()
    t6 = threading.Thread(target=draw_expression_lines,args=(turtles[5],'right',))
    t6.start()

#run all application
def execute():
    window = create_screen()
    #Array to store all cursors
    turtles = []
    #create one cursor for each thread
    for _ in range(6):
        turtles.append(get_turtle())

    start_threads(turtles)
    window.exitonclick()

#only execute if is a main class
if __name__ == '__main__':
    execute()
