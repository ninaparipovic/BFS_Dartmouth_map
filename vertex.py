# Nina Paripovic
# Lab 3 checkpoint
from cs1lib import *


class Vertex:
    def __init__(self, name, x_location, y_location):
        self.name = str(name)               # name of the vertex
        self.x_location = int(x_location)   # x coordinate of the location
        self.y_location = int(y_location)   # y coordinate of the location
        self.adjacency_list = []            # list that stores references to the adjacent vertex objects for the
        # vertex object that self references

    # method that appends an adjacent vertex object to the adjacency list
    def append_adjacency(self, vertex_object):
        self.adjacency_list.append(vertex_object)

    # coverts the adjacency list from a list of strings to a string with commas separating each adjacent vertex name
    def adjacency_list_reference(self):
            x = ''
            for i in range(len(self.adjacency_list)):
                if i == len(self.adjacency_list) - 1:
                    x += ' ' + str(self.adjacency_list[i].name)
                else:
                    x += ' ' + str(self.adjacency_list[i].name) + ','
            return x

    def __str__(self):
        return self.name + '; ' + 'Location: ' + str(self.x_location) + ', ' + str(self.y_location) + ';' + \
                ' Adjacent vertices:' + self.adjacency_list_reference()

    def draw_vertex(self, color, radius):
        disable_stroke()
        set_fill_color(*color)
        draw_circle(self.x_location, self.y_location, radius)

    def draw_edge(self, adjacent_vertex, color, width):
        enable_stroke()
        set_stroke_color(*color)
        set_stroke_width(width)
        draw_line(self.x_location, self.y_location, adjacent_vertex.x_location, adjacent_vertex.y_location)

    def draw_edges(self, color, width):
        enable_stroke()
        set_stroke_color(*color)
        set_stroke_width(width)
        for i in range(len(self.adjacency_list)):
            self.draw_edge(self.adjacency_list[i], color, width)

    def smallest_surrounding_square(self, x_coordinate, y_coordinate, radius):
        return self.x_location - radius <= x_coordinate <= self.x_location + radius \
            and self.y_location - radius <= y_coordinate <= self.y_location + radius
