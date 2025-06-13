import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bunga Cantik")

bunga = turtle.Turtle()
bunga.speed(3)
bunga.pensize(2)
bunga.hideturtle()

daun = turtle.Turtle()
daun.color("green")
daun.pensize(3)
daun.hideturtle()
daun.speed(2)

def kelopak(radius, angle, warna):
    bunga.color(warna)
    bunga.begin_fill()
    for _ in range(2):
        bunga.circle(radius, angle)
        bunga.left(180 - angle)
    bunga.end_fill()

jumlah_kelopak = 12
hue = 0
for i in range(jumlah_kelopak):
    bunga.penup()
    bunga.goto(0, 0)
    bunga.setheading(i * (360 / jumlah_kelopak))
    bunga.pendown()

    warna_rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    warna_rgb = tuple([round(c * 255) for c in warna_rgb])
    warna_hex = "#%02x%02x%02x" % warna_rgb

    kelopak(100, 60, warna_hex)
    hue += 1 / jumlah_kelopak

bunga.penup()
bunga.goto(0, -20)
bunga.setheading(0)
bunga.color("yellow")
bunga.pendown()
bunga.begin_fill()
bunga.circle(20)
bunga.end_fill()

daun.penup()
daun.goto(-40, -100)
daun.setheading(-60)
daun.pendown()
daun.begin_fill()
for _ in range(2):
    daun.circle(60, 60)
    daun.left(120)
daun.end_fill()

daun.penup()
daun.goto(40, -100)
daun.setheading(-120)
daun.pendown()
daun.begin_fill()
for _ in range(2):
    daun.circle(60, 60)
    daun.left(120)
daun.end_fill()

# Selesai
screen.mainloop()
