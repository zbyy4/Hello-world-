import turtle

tt = turtle.Turtle()

def polygon(side,length):
    angle = 360/side
    for i in range(side):
        tt.forward(length)
        tt.left(angle)

polygon(100,5)

tt.screen.mainloop()