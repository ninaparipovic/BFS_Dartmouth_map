from collections import deque


def breadth_first_search(start_vertex, goal_vertex):
    dictionary = {}

    dictionary[start_vertex.name] = None
    q = deque()
    q.append(start_vertex)

    # while the queue is not empty, continue to search for vertices
    while len(q) > 0:
        vertex = q.popleft()
        for i in range(len(vertex.adjacency_list)):
            if vertex.adjacency_list[i].name not in dictionary:
                # add the vertex to the dictionary with the vertex name as the key and its back-pointer as the value
                dictionary[vertex.adjacency_list[i].name] = vertex
                q.append(vertex.adjacency_list[i])

    # Create a list of vertex objects that connect the start and goal vertex.
    bfs_list = []
    bfs_list.append(goal_vertex)    # Append the goal vertex to the list.
    current_vertex = goal_vertex    # Make the goal vertex the current vertex.

    # Look up the goal vertex in the dictionary and make previous_vertex reference the value (which is a reference to
    # the back-pointer vertex object). Continue to find the back pointer by looking up the current vertex object in the
    # dictionary until the start vertex has been added to the list.
    while start_vertex not in bfs_list:
        previous_vertex = dictionary[current_vertex.name]
        bfs_list.append(previous_vertex)
        current_vertex = previous_vertex

    return bfs_list
