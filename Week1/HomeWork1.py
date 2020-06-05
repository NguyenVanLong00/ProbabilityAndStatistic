# homework week 1 :  write fuction seq_sum and  

import numpy as np

def seq_sum(k):
	Seq_of_coin_flip = [ int(x*2) for x in np.random.rand(k)]
	#print(Seq_of_coin_flip)
	return sum(Seq_of_coin_flip)
x = seq_sum(100)
print(x)
print([seq_sum(2) for x in range(20)])

def isInRange(n,k1,k2):
	if n>=k1 and n<k2:
		return True
	else:
		return False

def estimate_prob(n,k1,k2,m):
	timeInRange =0
	for i in range(m):
		numberOfHead = seq_sum(n)
		timeInRange = timeInRange+1 if isInRange(numberOfHead,k1,k2) else timeInRange
	return timeInRange/m

x=estimate_prob(100,45,55,1000)
print(type(x))
assert 'float' in str(type(x))
