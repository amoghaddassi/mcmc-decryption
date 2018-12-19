# Markov Chain Monte Carlo Decryption

Using MCMC and bigram letter transition probabilities to decode simple replacement cyphers.
\nAlso uses these chains to generate random sentences according to certain transition probabilities.
\nPurpose of each file is as follows:
	\nchain.py: Has the classes for an edge, graph, and Markov Chain.
	\nbigram_helpers.py: Has various helper functions for getting transition probabilites from a text file.
	\ndecrypt.py: Runs the MCMC algorithim to decode a given cypher (also has functions for generating replacement cyphers).
