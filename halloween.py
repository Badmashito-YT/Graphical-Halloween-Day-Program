import turtle
window = turtle.Screen()

ani = turtle.Turtle()
ani.shape("turtle")
#ani.speed(3) #slowest1,slow3,normal6,fast10,fastest0

#The Pumkin
ani.penup()
ani.goto(0,-150)
ani.color("#ff6600")
ani.begin_fill()
ani.circle(150)
ani.end_fill()

#Position of the Lefft Eye
ani.goto(-110,10)
ani.color("white")

#Making of the Left Eye
ani.pendown()
ani.begin_fill()
ani.left(60)
ani.fd(80)  
ani.right(120)
ani.fd(80)  
ani.right(120)
ani.fd(80)
ani.end_fill()

ani.penup()
ani.right(180)
ani.fd(130)
ani.pendown()

#Making of the Right Eye
ani.begin_fill()
ani.left(60)
ani.fd(80)  
ani.right(120)
ani.fd(80)
ani.right(120)
ani.fd(80)
ani.end_fill()

#Fixing the cursor for the Teeth
ani.penup()
ani.fd(110)
ani.left(90)
ani.fd(100)
ani.left(90)
ani.pendown()

#Making of the Teeths
for x in range(6):
    ani.begin_fill()
    ani.left(60)
    ani.fd(30)  
    ani.right(120)
    ani.fd(30)  
    ani.right(120)
    ani.fd(30)
    ani.end_fill()

    ani.right(180)
    ani.fd(30)

#Fixing the cursor for the Stump of the Pumkin
ani.penup()
ani.left(120)
ani.fd(269)
ani.pendown()

#Making of the Stump of the Pumkin
ani.color("brown")
ani.begin_fill()
ani.right(30)
ani.fd(40)
ani.right(90)
ani.fd(90)
ani.right(90)
ani.fd(40)
ani.end_fill()

#Happy  Halloween 
ani.penup()
ani.goto(-100,-235)
ani.color("red")
ani.write("Happy Halloween !", font = ["Arial",24,"normal"] )



window.exitonclick()


