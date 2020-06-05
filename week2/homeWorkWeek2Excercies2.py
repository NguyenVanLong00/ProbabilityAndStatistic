from itertools import product

A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}


def product_of_unions(A,B,S,T):
	unionOfAB= set.union(A,B)
	unionOfST= set.union(S,T)

	final_product = set(product(unionOfAB,unionOfST))
	return (unionOfAB,final_product)

product_of_unions(A,B,S,T)

def t(A,B,S,T):
	
    return (set(product(A,S)),set.union(product(A,S),product(A,T),product(B,S),product(B,T)))