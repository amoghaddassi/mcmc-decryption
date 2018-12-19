# Markov Chain Monte Carlo Decryption

Using MCMC and bigram letter transition probabilities to decode simple replacement cyphers.
Also uses these chains to generate random sentences according to certain transition probabilities.
Purpose of each file is as follows:
	chain.py: Has the classes for an edge, graph, and Markov Chain.
	bigram_helpers.py: Has various helper functions for getting transition probabilites from a text file.
	decrypt.py: Runs the MCMC algorithim to decode a given cypher (also has functions for generating replacement cyphers).
