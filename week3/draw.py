# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from tkinter import Y, Canvas
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)

    # Call the draw_sky and draw_ground functions in this file.
    # draw_sky(canvas, 0, 0, 800, 500, 'skyBlue2')
    # draw_sky(canvas, 0, 0, 800, 275, 'lightSkyBlue2')
    # draw_sky(canvas, 0, 0, 800, 125, 'darkSeaGreen3')

    draw_cloud(canvas, 225, 360, 355, 420, 'azure' ,'azure')
    draw_cloud(canvas, 120, 425, 315, 485, 'azure' ,'azure')
    draw_cloud(canvas, 125, 370, 350, 470, 'azure' ,'azure')
    draw_cloud(canvas, 50, 380, 225, 455, 'azure2' ,'azure2')
    draw_cloud(canvas, 100, 350, 265, 415, 'azure' ,'azure')
    draw_cloud(canvas, 250, 400, 400, 480, 'azure2' ,'azure2')


    draw_cloud(canvas, 400, 300, 725, 360, 'azure' ,'azure')
    draw_cloud(canvas, 450, 300, 770, 410, 'azure' ,'azure')
    draw_cloud(canvas, 480, 375, 625, 425, 'azure' ,'azure')
    draw_cloud(canvas, 560, 285, 725, 350, 'azure' ,'azure')
    #lowest
    draw_temple(canvas, 140, 50, 360, 130, 'black', 'aliceBlue')
    #second lowest
    draw_temple(canvas, 160, 50, 340, 175, 'black', 'aliceBlue')
    #narrow tall one
    draw_temple(canvas, 225, 50, 275, 225, 'black', 'aliceBlue')
    draw_temple(canvas, 200, 50, 300, 210, 'black', 'aliceBlue')
    #left window
    draw_temple(canvas, 175, 75, 185, 150, 'black', 'lightBlue2')
    #right window
    draw_temple(canvas, 315, 75, 325, 150, 'black', 'lightBlue2')
    #middle window
    draw_temple(canvas, 235, 65, 265, 130, 'black', 'lightBlue2')
    #middle window
    draw_temple(canvas, 235, 145, 265, 190, 'black', 'lightBlue2')
    #bottom
    draw_temple(canvas, 120, 40, 380, 50, 'black', 'aliceBlue')


    finish_drawing(canvas)



def draw_sky(canvas, x0, y0, x1, y1, color):
    draw_rectangle(canvas, x0, y0, x1, y1, width=0, fill=color)
    pass

def draw_cloud(canvas, x0, y0, x1, y1, color1, color2):
    draw_oval(canvas, x0, y0, x1, y1, outline=color1, fill=color2)
    pass
   

def draw_temple(canvas, x0, y0, x1, y1, color1, color2):
    draw_rectangle(canvas, x0, y0, x1, y1, outline=color1, fill=color2)
    pass


def draw_grid(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()