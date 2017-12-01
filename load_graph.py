# load_graph.py
# Cindy Zhu
# Create vertex dictionary

from vertex import Vertex

def load_graph(file_name):

    # vertex dictionary
    vertex_dict = {}

    # list to store information from file
    info_list = []

    # open file for reading
    f = open(file_name, 'r')

    # append each line of the file to info_list
    for line in f:
        info_list.append(line)

    # close file
    f.close()

    # go through info_list for the first time, adding the vertex's name and location
    for index in info_list:

        vertex_info = index.split(";") # split each index of info_list by semicolon
        vertex_name = vertex_info[0].strip() # vertex name = 0th index of already split line

        vertex_location = vertex_info[2].split(",") # location = 2nd index of already split line, so split by comma
        vertex_x = int(vertex_location[0].strip()) # x location = 0th index of 2nd index split by comma
        vertex_y = int(vertex_location[1].strip()) # y location = 1st index of 2nd index split by comma

        vertex_dict[vertex_name] = Vertex(vertex_name, vertex_x, vertex_y) # add vertex information to dictionary

    # go through info_list for the second time, adding information about adjacent vertices
    for index in info_list:

        vertex_info = index.split(";") # split line by semicolon
        vertex_name = vertex_info[0].strip() # vertex name = 0th index of already split line

        adjacent_vertices = vertex_info[1].split(",") # split 1st index of already split line by comma to get adjacents

        # add each adjacent vertex to the original vertex objects in the dictionary
        for adjacent_vertex in adjacent_vertices:
            vertex_dict[vertex_name].adjacents.append(vertex_dict[adjacent_vertex.strip()])

    return vertex_dict

