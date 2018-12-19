from bigram_helpers import *
from chain import *

import numpy as np
import math
from random import shuffle

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

def decrypt(string, runs=1000, letter_trans_mc=bigram_mc('data/warandpeace.txt')):
    """Runs the Metroplis MCMC algorithim to decrypt the string (encrypted by replacement)
    using mc as the letter transition chain."""
    decoder = get_random_decoder()
    res_string = encoder(string, decoder)
    res_score = letter_trans_mc.prob_of_path(res_string)
        
    for _ in range(runs):
        proposed_decoder = get_new_decoder(decoder)
        prop_string = encoder(string, proposed_decoder)
        prop_score = letter_trans_mc.prob_of_path(prop_string)
        
        # TODO: Get score comparison working, problem is that the values are too close to 0.
        score_ratio = prop_score / res_score
        if score_ratio > np.random.uniform():
            decoder, res_score, res_string = proposed_decoder, prop_score, prop_string
        print(res_string)
    return res_string

def get_random_decoder():
    """Generates a random 26 letter decoder (spaces remain the same)."""
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    shuffled = alpha.copy() 
    shuffle(shuffled)
    return {key:value for (key, value) in zip(alpha, shuffled)}

def get_new_decoder(decoder):
    """Returns a new decoder with exactly two different mappings
    This is to ensure that our transition matrix for MCMC is symmetric."""
    res = decoder.copy()
    letters = np.random.choice(list(decoder.keys()), 2, replace=False)
    l0, l1 = letters[0], letters[1]
    res[l0] = decoder[l1]
    res[l1] = decoder[l0]
    return res

def encoder(string, coder):
    """Maps string to result with coder.
    coder: a dictionary with keys of the letters in string and values of the letters in return string."""
    res = ''
    for char in list(string):
        if char in coder:
            res += coder[char]
        else:
            res += char
    return res

def invert_cypher(cypher):
    pass

def random_sentence(n, chain):
    """Generates a random sentence of length n according to the chain."""
    return ''.join([edge.name for edge in chain.path(n)])
