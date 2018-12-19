#Creates an alphabet to reference when creating the chain and making bigrams.
states = list('abcdefghijklmnopqrstuvwxyz ')

def bigram_from_file(src):
    """Will create a bigram transition matrix using a text file at src."""
    file_obj = open(src, 'r', encoding='utf-8')
    text = split_text(file_obj.read())
    transition_matrix = bigram_matrix(text)
    return transition_matrix

def bigram_matrix(string):
    """Returns a dictionary of transition probabilities from a given string"""
    #create all possible pairs of letters
    pairs = []
    for l1 in states:
        for l2 in states:
            pairs.append((l1, l2))
    
    #iterate through string and keep counts of letter pairs
    probs = {pair:0 for pair in pairs}
    str_lst = list(string)
    for i in range(len(string)-1):
        probs[(str_lst[i], str_lst[i+1])] += 1
    return probs

def split_text(string):
    """Removes any special chars to make bigram matrices 27*27 (including spaces)."""
    string = string.replace("\n"," ")
    return "".join([i for i in string.lower().strip() if i in states])

def get_alpha_index(letter):
    """Returns the position of letter in a list of alphabets."""
    index = 0
    for l in list('abcdefghijklmnopqrstuvwxyz '):
        if letter == l:
            return index
        index += 1

