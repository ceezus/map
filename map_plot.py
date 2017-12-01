# map_plot.py
# Cindy Zhu

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

# window height and width
WINDOW_HEIGHT = 811
WINDOW_WIDTH = 1012

# state variables
start = None
goal = None
goal_found = False
start_found = False

# vertex dictionary
vertex_dict = load_graph("dartmouth_graph.txt")

# load map
def pic(img):
    draw_image(load_image(img), 0, 0)

def main():
    global start, goal, goal_found, start_found

    # load map
    pic("dartmouth_map.png")

    # draw each vertex & the connect-y line things in blue
    for location in vertex_dict:
        vertex_dict[location].draw_vertex(0, 0, 1)
        vertex_dict[location].draw_edges(0, 0, 1)

    # if the mouse is pressed
    if is_mouse_pressed():

        # loop through vertex_dict
        for location in vertex_dict:

            # if the mouse is in the square that inscribes a vertex circle
            if vertex_dict[location].select_vertex(mouse_x(), mouse_y()):

                start = vertex_dict[location] # start = the vertex you click on
                start.draw_vertex(1, 0, 0) # make vertex red
                start_found = True # start has now been found
                break # stop loop

    # once start is found, find goal
    if start_found:

        # loop through vertex dictionary
        for location in vertex_dict:
            # if it's the same vertex, continue
            if vertex_dict[location] == start:
                continue
            # if the mouse is in the square around the vertex, that vertex = goal
            if vertex_dict[location].select_vertex(mouse_x(), mouse_y()):

                goal = vertex_dict[location] # goal = whatever vertex your mouse is hovering over
                goal.draw_vertex(1, 0, 0) # draw in red
                goal_found = True # goal has been found
                break # stop loop

    # once the goal and start have been found, implement breadth-first search
    if start_found and goal_found:
        path = bfs(start, goal) # path = bfs from start to goal
        goal = path[0] # goal = first element of path
        previous = goal
        # draw path from start to goal in red
        for vertex in path:
            vertex.draw_vertex(1, 0, 0)
            vertex.draw_path(previous, 1, 0, 0)
            previous = vertex 


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)