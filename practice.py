import turtle

tt = turtle.Turtle()

def polygon(side,length):
    angle = 360/side
    for i in range(side):
        tt.forward(length)
        tt.left(angle)

polygon(6,100)

tt.screen.mainloop()