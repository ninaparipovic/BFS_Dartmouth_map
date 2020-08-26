# Nina Paripovic
# Lab 3 extra credit
# Nov 5th 2018
from load_graph import *
from cs1lib import *
from bfs import *


IMAGE_WIDTH = 1012
IMAGE_HEIGHT = 811
TEAL = (0, 0.5, 0.5)
RED = (1, 0, 0)
VERTEX_RADIUS = 6
EDGE_WIDTH = 3
mouse_x = 0
mouse_y = 0

start_vertex = None
goal_vertex = None
button_down = False
hovering_over = False


def map_plot(img):
    global start_vertex, goal_vertex, hovering_over
    clear()
    draw_image(img, 0, 0)   # draw the Dartmouth map
    vertex_dict = load_graph('lab3/dartmouth_graph.txt')
    # draw all the vertices in the dictionary imported from the text file and draw the edges between vertices
    for key in vertex_dict:
        vertex = vertex_dict[key]
        vertex.draw_vertex(TEAL, VERTEX_RADIUS)
        vertex.draw_edges(TEAL, EDGE_WIDTH)

    # if the mouse has been pressed, search through the vertices in the dictionary and if the mouse press event occurred
    # within the smallest surrounding square of any vertex, make that vertex the starting vertex and draw it red
    if button_down:
        for key in vertex_dict:
            vertex = vertex_dict[key]
            if vertex.smallest_surrounding_square(mouse_x, mouse_y, VERTEX_RADIUS):
                start_vertex = vertex

    # if there is a current start vertex, search through the vertices in the dictionary and if the mouse is hovering
    #  within the smallest surrounding square of any vertex, make that vertex the goal vertex and draw it red
    if start_vertex != None:
        hovering_over = False
        for key in vertex_dict:
            vertex = vertex_dict[key]

            if vertex.smallest_surrounding_square(mouse_x, mouse_y, VERTEX_RADIUS):
                hovering_over = True
                goal_vertex = vertex
                goal_vertex.draw_vertex(RED, VERTEX_RADIUS)

        if not hovering_over:
            goal_vertex = None

    # perform breadth-first-search if there is a current start and goal vertex and if they are not referencing the
    # same vertex object. Draw the path between the start and goal vertices in red.
    if start_vertex != None and goal_vertex != None and start_vertex.name != goal_vertex.name:
        bfs_list = breadth_first_search(start_vertex, goal_vertex)
        for i in range(len(bfs_list)-1):
            vertex = bfs_list[i]
            next_vertex = bfs_list[i+1]
            vertex.draw_edge(next_vertex, RED, EDGE_WIDTH)
            vertex.draw_vertex(RED, VERTEX_RADIUS)

    # if there is a current start vertex, draw the vertex in red and write the vertex name above it
    if start_vertex != None:
            start_vertex.draw_vertex(RED, VERTEX_RADIUS)
            enable_stroke()
            set_stroke_color(0.25, 0, 0.5)
            draw_text(start_vertex.name, start_vertex.x_location - 8, start_vertex.y_location - 8)

    # if there is a current goal vertex, write the vertex name above it
    if goal_vertex != None:
        enable_stroke()
        set_stroke_color(0.25, 0, 0.5)
        draw_text(goal_vertex.name, goal_vertex.x_location - 8, goal_vertex.y_location - 8)

# update the mouse position if the mouse is moved.
def mouse_move(mx, my):
    global mouse_x, mouse_y
    mouse_x = mx
    mouse_y = my

# register when the mouse has been pressed.
def mouse_down(mx, my):
    global button_down, mouse_x, mouse_y
    button_down = True
    mouse_x = mx
    mouse_y = my


# register when the mouse has been released.
def mouse_up(mx, my):
    global button_down, mouse_x, mouse_y
    button_down = False
    mouse_x = mx
    mouse_y = my


def main():
    map_plot(img)


img = load_image('lab3/dartmouth_map.png')

start_graphics(main, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, mouse_press=mouse_down, mouse_move=mouse_move,
               mouse_release=mouse_up)
