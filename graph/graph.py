#!/usr/bin/env python
""" Implementation of graph ADT """

class Edge:
    """
    Data:
    element: Returns the item stored
    Method:
    endpoints(): returns a tuple (u, v), u is origin and v is destination
            opposite(v): If one endpoint is v, then what is/are the other endpoint(s)
    """
    pass

class Vertex:
    """
    Data:
    element : Returns the item stored
    """
    pass



class Graph:
    """
    Data:
    Methods:
        vertex_count()
        vertices()
        edge_count()
        edges()
        get_edge(u, v)
        degree(v, out=True)
        incident_edges(v, out=True): Returns iterattion of all the edges
        insert_vertex(x=None): element x to be stored
        insert_edge(u, v, x=None): element x to be stored
        remove_vertex(v)
        remove_edge(e)
    """
    pass
