# bfs.py
# Cindy Zhu
# implementation of breadth-first search

from collections import deque

def bfs(start, goal):

    frontier = deque() # frontier is double ended queue
    frontier.append(start) # append starting vertex to queue

    backpointers = {} # backpointers dictionary

    # while frontier is not empty
    while len(frontier) > 0:
        current_vertex = frontier.popleft() # remove current vertex

        if current_vertex == goal: # if current vertex is the goal
            path = [goal] # create path, starting from goal

            # append backpointers until start vertex
            while current_vertex != start:
                current_vertex = backpointers[current_vertex]
                path.append(current_vertex)

            return path

        # if the current vertex is not the goal
        else:
            # loop through adjacents to the vertex
            for adjacent_vertex in current_vertex.adjacents:

                # if this adjacent is not a backpointer
                if not adjacent_vertex in backpointers:

                    # assign backpointer
                    backpointers[adjacent_vertex] = current_vertex
                    # append to frontier
                    frontier.append(adjacent_vertex)
