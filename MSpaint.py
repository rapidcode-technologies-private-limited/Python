import tkinter

print(
    "to draw a picture or something,hold down your left mouse button and move your mouse around to make something,VERY artistic.")
print("to change your brush color since you don't like black as your color,click on one of the colour 'boxes.'")
window = tkinter.Tk()
Canvas = tkinter.Canvas(window, width=750, height=500, bg='white')
Canvas.pack()
colour = "black"
lastX, lastY = 0 , 0


def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y


def on_click(event):
    store_position(event)


def on_drag(event):
    Canvas.create_line(lastX,lastY, event.x, event.y, fill=colour, width=3)
    store_position(event)


Canvas.bind("<Button-1>", on_click)
Canvas.bind("<B1-Motion>", on_drag)

red_id = Canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = Canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = Canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = Canvas.create_rectangle(10, 85, 30, 105, fill="white")
orange_id = Canvas.create_rectangle(10, 110, 30, 130, fill="orange")
brown_id = Canvas.create_rectangle(10, 135, 30, 155, fill="saddlebrown")
yellow_id = Canvas.create_rectangle(10, 160, 30, 180, fill="yellow")
gold_id = Canvas.create_rectangle(10, 185, 30, 205, fill="gold")
peach_id = Canvas.create_rectangle(10, 210, 30, 230, fill="bisque")
green_id = Canvas.create_rectangle(10, 235, 30, 255, fill="limegreen")
lime_id = Canvas.create_rectangle(10, 260, 30, 280, fill="lime")
cyan_id = Canvas.create_rectangle(10, 285, 30, 305, fill="cyan")
blue_id = Canvas.create_rectangle(10, 310, 30, 330, fill="blue")
indigo_id = Canvas.create_rectangle(10, 335, 30, 355, fill="indigo")
purple_id = Canvas.create_rectangle(10, 360, 30, 380, fill="purple")
magenta_id = Canvas.create_rectangle(10, 385, 30, 405, fill="magenta")
pink_id = Canvas.create_rectangle(10, 410, 30, 430, fill="pink")
grey_id = Canvas.create_rectangle(10, 435, 30, 455, fill="grey")
aliceblue_id = Canvas.create_rectangle(10, 460, 30, 480, fill="aliceblue")


def set_colour_red(event):
    global colour
    colour = "red"


def set_colour_blue(event):
    global colour
    colour = "blue"


def set_colour_black(event):
    global colour
    colour = "black"


def set_colour_white(event):
    global colour
    colour = "white"


def set_colour_orange(event):
    global colour
    colour = "orange"


def set_colour_brown(event):
    global colour
    colour = "brown"


def set_colour_yellow(event):
    global colour
    colour = "yellow"


def set_colour_gold(event):
    global colour
    colour = "gold"


def set_colour_peach(event):
    global colour
    colour = "bisque"


def set_colour_green(event):
    global colour
    colour = "limegreen"


def set_colour_lime(event):
    global colour
    colour = "lime"


def set_colour_cyan(event):
    global colour
    colour = "cyan"


def set_colour_blue(event):
    global colour
    colour = "blue"


def set_colour_indigo(event):
    global colour
    colour = "indigo"


def set_colour_purple(event):
    global colour
    colour = "purple"


def set_colour_magenta(event):
    global colour
    colour = "magenta"


def set_colour_pink(event):
    global colour
    colour = "pink"


def set_colour_grey(event):
    global colour
    colour = "grey"


def set_colour_aliceblue(event):
    global colour
    colour = "aliceblue"


Canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
Canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
Canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
Canvas.tag_bind(white_id, "<Button-1>", set_colour_white)
Canvas.tag_bind(orange_id, "<Button-1>", set_colour_orange)
Canvas.tag_bind(brown_id, "<Button-1>", set_colour_brown)
Canvas.tag_bind(yellow_id, "<Button-1>", set_colour_yellow)
Canvas.tag_bind(gold_id, "<Button-1>", set_colour_gold)
Canvas.tag_bind(peach_id, "<Button-1>", set_colour_peach)
Canvas.tag_bind(green_id, "<Button-1>", set_colour_green)
Canvas.tag_bind(lime_id, "<Button-1>", set_colour_lime)
Canvas.tag_bind(cyan_id, "<Button-1>", set_colour_cyan)
Canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
Canvas.tag_bind(indigo_id, "<Button-1>", set_colour_indigo)
Canvas.tag_bind(purple_id, "<Button-1>", set_colour_purple)
Canvas.tag_bind(magenta_id, "<Button-1>", set_colour_magenta)
Canvas.tag_bind(pink_id, "<Button-1>", set_colour_pink)
Canvas.tag_bind(grey_id, "<Button-1>", set_colour_grey)
Canvas.tag_bind(aliceblue_id, "<Button-1>", set_colour_aliceblue)

window.mainloop()




