from bigram_helpers import *
from chain import *

def bigram_mc(src):
    """Constructs a transition matrix based on the proporitions 
    of the text file at src."""
    transition_probs = bigram_from_file(src)
    letters = list('abcdefghijklmnopqrstuvwxyz ')
    edges = []
    for l1 in letters:
        probs = []    
        for l2 in letters:
            probs.append(transition_probs[(l1, l2)])
        edges.append(Edge(probs, name=l1))
    return Chain(edges)

def random_sentence(n, chain):
    """Generates a random sentence of length n according to the chain."""
    return ''.join([edge.name for edge in chain.path(n)])
