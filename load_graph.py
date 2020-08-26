# Nina Paripovic
# Lab 3 checkpoint
from vertex import Vertex


# Function which reads through a file and creates a vertex object for each line of code. Each vertex object is added
# to a dictionary with the name of the vertex object as the key and the adjacency list of the vertex object as the value
def load_graph(file_name):
    f = open(file_name, 'r')    # open the file

    # Dictionary which stores all the vertex objects.
    dictionary = {}
    # List which stores all the lines of code
    vertices_list = []

    for line in f:
        # Append each line to vertices_list as a string for the second pass through the file reading.
        vertices_list.append(str(line))
        # Split object into 3 parts, object name, adjacent vertices and x and y coordinates.
        object = line.strip().split(';')
        # Separate the x and y coordinates.
        vertex_coordinates = object[2].split(',')
        # Create a vertex object for each line of the file.
        vertex = Vertex(str(object[0]), int(vertex_coordinates[0]), int(vertex_coordinates[1]))
        # Add the vertex to the dictionary by using the name of the vertex as the key and
        # make the dictionary entry reference the corresponding vertex object
        dictionary[vertex.name] = vertex

        # Read through the data a second time.
    for item in vertices_list:
        # Split the list into 3 parts.
        thing = item.split(';')
        vertex_name = thing[0]
        adjacent_vertices = thing[1].strip().split(',')     # create a list of adjacent vertices for the vertex object.

        # Access the vertex object by looking it up in the dictionary using the vertex name as the key.
        current_vertex = dictionary[str(vertex_name)]
        for i in range(len(adjacent_vertices)):
            # creates reference to adjacent_vertex object.
            adjacent_vertex = adjacent_vertices[i].strip()
            # Look up the adjacent vertex in the dictionary which returns a reference to the adjacent vertex object.
            adjacent_vertex = dictionary[adjacent_vertex]

            # Append the reference to the adjacent vertex object to the adjacency list of the current vertex object
            # and store the list as the value of the dictionary entry for the current vertex object.
            current_vertex.append_adjacency(adjacent_vertex)


    f.close()   # close the file

    # return a reference to the dictionary containing all the vertex objects
    return dictionary
