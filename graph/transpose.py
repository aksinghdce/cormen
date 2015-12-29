#!/usr/bin/env python
""" Calculate transpose of a graph """

class Node:
    """Vertex of a graph"""
    def __init__(self, adj_list=None):
        """ the adjacency list of a vertex can be initialized"""
        if adj_list is None:
            self.adj_list = list()
        self.adj_list = adj_list
    def add_edge(self, v):
        self.adj_list.append(v)
    def remove_edge(self, v):
        if v in self.adj_list:
            self.adj_list.remove(v)

class Graph:
    """ A graph class """
    def __init__(self, n):
        """
        constructs a random graph with maximum n vertices
        """
        self.G = 

def transpose(G):
    """Calculates transpose of a graph G
    G: adjacency list representation
    specifically G is a list of lists
    """

