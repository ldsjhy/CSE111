# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def draw_pine_tree(canvas, center_x, bottom, height):
    # draw the trunk of the tree.
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")
    # Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")

# def draw_fence(canvas, center_x):

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    draw_ground(canvas)
    draw_sun(canvas)
    draw_cloud(canvas)
    draw_pine_tree(canvas, 240, 70, 380)
    draw_pine_tree(canvas, 160, 30, 400)
    draw_pine_tree(canvas, 100, 10, 400)
    for x in range(25, 800, 50):
        draw_fence(canvas, x, 0, 200)

    # draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_grid(canvas, width, height, interval):
    # draw vertical lines
    label_y = 15 
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    # draw vertical lines
    label_x = 15 
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

def draw_sky(canvas):
    draw_rectangle(canvas, 0, 0, 800, 500, fill="skyblue")

def draw_sun(canvas):
    draw_oval(canvas, 720, 520, 820, 420, fill="gold1", outline="gold1")

def draw_cloud(canvas):
    draw_oval(canvas, 100, 400, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 120, 430, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 300, 400, 400, 350, fill="white", outline="white")
    draw_oval(canvas, 320, 400, 400, 350, fill="white", outline="white")
    draw_oval(canvas, 650, 375, 750, 425, fill="white", outline="white")
    draw_oval(canvas, 620, 400, 800, 350, fill="white", outline="white")
    draw_oval(canvas, 620, 400, 700, 350, fill="white", outline="white")
    draw_oval(canvas, 520, 300, 610, 250, fill="white", outline="white")

def draw_ground(canvas):
    draw_rectangle(canvas, 0, 0, 800, 100, fill="saddleBrown", outline="saddleBrown")

def draw_fence(canvas, center_x, bottom, height):
    skirt_width = height / 200 * 40
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_bottom = bottom
    peak_x = center_x
    peak_y = height
    skirt_upper_height = bottom + height * 5 / 6
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_left, skirt_upper_height, peak_x, peak_y, skirt_right, skirt_upper_height, skirt_right, skirt_bottom, fill="white", outline="white")


# def draw_fence(canvas):
#     x_start = 0
#     y_start = 50
#     for i in range(10):
#         draw_rectangle(canvas, x_start, 0, y_start, 10, fill="white", outline="white")
#         y_start +=100
main()