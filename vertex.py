# vertex.py
# Cindy Zhu

from cs1lib import *

RADIUS = 8

class Vertex:

    # init method
    def __init__(self, name, x, y):
        self.name = name # name
        self.x = x # x location
        self.y = y # y location
        self.adjacents= [] # list of adjacents

    # method to get all adjacent vertices
    def adjacent_vertices(self):

        adjacent_vertexes = "" # empty string to store
        adjacent_index = 0 # start at index zero of list of adjacents

        # loop over list of adjacents
        for adjacent_vertex in self.adjacents:

            adjacent_index += 1 # add one to index

            # if the index is less than the length, add a comma after the name
            if adjacent_index < len(self.adjacents):
                adjacent_vertexes += adjacent_vertex.name + ", "
            # else, don't
            else:
                adjacent_vertexes += adjacent_vertex.name

        return adjacent_vertexes

    # draw vertex as a circle
    def draw_vertex(self, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    # draw path connecting vertices
    def draw_path(self, vertex, r, g, b):
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    # draw the lines that connect all the vertices
    def draw_edges(self, r, g, b):
        for vertex in self.adjacents:
            set_stroke_color(r, g, b)
            draw_line(self.x, self.y, vertex.x, vertex.y)

    # select vertex based on mouse proximity
    def select_vertex(self, x, y):
        return abs(x - self.x) <= RADIUS and abs(y - self.y) <= RADIUS

    # string method
    def __str__(self):
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + self.adjacent_vertices()