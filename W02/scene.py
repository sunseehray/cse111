# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    # draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in it"""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

    # cloud 1
    center_x = 650
    center_y = 400
    cloud_width = 200
    cloud_height = 50
    draw_cloud(canvas, center_x, center_y, cloud_width, cloud_height)

    # cloud 2
    center_x_2 = 600
    center_y_2 = 425
    cloud_width_2 = 200
    cloud_height_2 = 50
    draw_cloud(canvas, center_x_2, center_y_2, cloud_width_2, cloud_height_2)

    # cloud 3
    center_x_3 = 350
    center_y_3 = 350
    cloud_width_3 = 200
    cloud_height_3 = 50
    draw_cloud(canvas, center_x_3, center_y_3, cloud_width_3, cloud_height_3)

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="tan4")

    # pine tree
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    
    # round tree 1
    rtree1_center_x = 600
    rtree1_bottom = 125
    rtree1_trunk_width = 15
    rtree1_trunk_height = 125
    rtree1_head_width = 100
    rtree1_head_height = 110
    rtree1_color = 'chartreuse3'
    draw_round_tree(canvas, rtree1_center_x, rtree1_bottom, rtree1_trunk_width, rtree1_trunk_height, rtree1_head_width, rtree1_head_height, rtree1_color)

    # draw pool 1
    pool1_center_x = 325
    pool1_center_y = 125
    pool1_width = 170
    pool1_height = 40
    draw_water(canvas, pool1_center_x, pool1_center_y, pool1_width, pool1_height)

    # draw pool 2
    pool2_center_x = 450
    pool2_center_y = 100
    pool2_width = 250
    pool2_height = 70
    draw_water(canvas, pool2_center_x, pool2_center_y, pool2_width, pool2_height)

    # pine tree 2
    tree_center_x_2 = 75
    tree_bottom_2 = 50
    tree_height_2 = 300
    draw_pine_tree(canvas, tree_center_x_2, tree_bottom_2, tree_height_2)
 
    # round tree 2
    rtree2_center_x = 700
    rtree2_bottom = 75
    rtree2_trunk_width = 20
    rtree2_trunk_height = 150
    rtree2_head_width = 120
    rtree2_head_height = 200
    rtree2_color = 'chartreuse4'
    draw_round_tree(canvas, rtree2_center_x, rtree2_bottom, rtree2_trunk_width, rtree2_trunk_height, rtree2_head_width, rtree2_head_height, rtree2_color)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function will draw a pine tree.
        center_x, bottom: The x and y location in pixels where this function will draw the bottom
            of a pine tree.
        height: The height in pixels of the pine tree that this function will draw.
        Return: nothing
        """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline='gray20', width=1, fill="tan3")
    
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + skirt_height

    # draw the crown / skirt of the pine tree
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline='gray20', width=1, fill="dark green")

def draw_cloud(canvas, center_x, center_y, width, height):
    """Draw a single cloud
    Parameters
        canvas: The canvas where this function will draw a cloud.
        center_x, center_y: The location in pixels where this function will draw the cloud.
        width: The width in pixels of the cloud
        height: the height in pixels of the cloud
    Return: nothing
    """
    cloud_left = center_x - width / 2
    cloud_bottom = center_y - height / 2
    cloud_right = center_x + width / 2
    cloud_top = center_y + height / 2
    # draw cloud
    draw_oval(canvas, cloud_left, cloud_bottom, cloud_right, cloud_top, width=1, outline='white', fill='white')

def draw_round_tree(canvas, center_x, bottom, trunk_width, trunk_height, head_width, head_height, color):
    """Draw a tree with a round head
    Parameters
        canvas: the canvas where this function will draw a tree
        center_x: The location in pixels where this function will draw the tree
        bottom: the bottom of the tree
        trunk_width: width of the tree trunk
        trunk_height: height of the tree trunk
        head_width: width of the upper part of the three
        head_height: height of the upper part of the tree
        color: color of the head
    Return none
    """
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    # Draw the trunk of the tree
    draw_rectangle(canvas, trunk_left, bottom, trunk_right, trunk_top, outline='gray20', width=1, fill="tan3")

    head_left = center_x - head_width / 2
    head_right = center_x + head_width / 2
    head_bottom = bottom + trunk_height + (head_height / 2)
    head_top = bottom + trunk_height - (head_height / 2)
    # Draw the crown of the tree
    draw_oval(canvas, head_left, head_bottom, head_right, head_top, width=1, outline='gray20', fill=color)

def draw_water(canvas, center_x, center_y, width, height):
    """Draw a single water pool
    Parameters
        canvas: The canvas where this function will draw a cloud.
        center_x, center_y: The location in pixels where this function will draw the pool.
        width: The width in pixels of the pool
        height: the height in pixels of the pool
    Return: nothing
    """
    pool_left = center_x - width / 2
    pool_bottom = center_y - height / 2
    pool_right = center_x + width / 2
    pool_top = center_y + height / 2
    # draw pool
    draw_oval(canvas, pool_left, pool_bottom, pool_right, pool_top, width=1, outline='blue1', fill='blue1')

def draw_grid(canvas, width, height, interval, color="blue"):
    """Draw grid taken from Documentation to use as temporary guide/reference
    """
    # draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)
    
    #draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
# Call the main function so that
# this program will start executing.
main()