from bigram_helpers import *
import numpy as np

class Edge:
    def __init__(self, weights, name=None):
        # assert sum(weights) == 1, 'Transfer probabilities must be normalized'
        self.weights = weights
        self.normalize() #Decided to just normalize here instead of when calling the constructor.
        if name:
            self.name = name

    def pick_node(self):
        return np.random.choice(range(len(self.weights)), p = self.weights)

    def normalize(self):
        """Normalizes weights vector to unit length."""
        total = sum(self.weights)
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] / total

    def prob_of_transition(self, node):
        """Finds the prob of going to node, where node is some alphabet.
        Assumes that the weights list is in alphabetic order"""
        return self.weights[get_alpha_index(node.name)]
        letter = node.name
        
    def __str__(self):
        res = '('
        for weight in list(self.weights)[:len(self.weights)-1]:
            res += str(weight) + ', '
        return res + str(self.weights[len(self.weights)-1]) + ')'

    def __repr__(self):
        return str(self.name)

class Graph:
    def __init__(self, edges):
        self.edges = edges

    def __str__(self):
        res = '['
        for edge in self.edges[:len(self.edges)-1]:
            res += edge.__str__() + '\n'
        return res + str(self.edges[len(self.edges)-1]) + ']'

class Chain(Graph):
    def __init__(self, edges):
        for i in edges:
            for j in edges:
                if i != j: assert len(i.weights) == len(j.weights), 'Transfer matrix must be square.'
        self.edges = edges
        self.node = np.random.choice(self.edges)

    def transfer(self):
        self.node = self.edges[self.node.pick_node()]

    def path(self, n):
        """Simulates a path of length n, changing the node of the graph."""
        path = []
        for _ in range(n):
            new_node = self.edges[self.node.pick_node()]
            path.append(new_node)
            self.node = new_node
        return path

    def prob_of_path(self, path):
        """Finds probability of a path, which is a list of states."""
        prob = 1
        for i in range(len(path)-1):
            curr_node = [edge for edge in self.edges if edge.name == path[i]][0]
            next_node = [edge for edge in self.edges if edge.name == path[i+1]][0] 
            prob *= curr_node.prob_of_transition(next_node)
        return prob

    def steady_state(self, reps=1000):
        props = []
        path = self.path(reps)
        for edge in self.edges:
            prop = [edge is i for i in path]
            props.append(np.count_nonzero(prop) / reps)
        return props

