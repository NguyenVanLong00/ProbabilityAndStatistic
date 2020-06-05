import numpy 

def generate_counts(k=1000,n=10):
	X = numpy.matrix(2* (numpy.random.rand(k,n)>0.5)-1) # generate matrix of -1 and 1
	S = X.sum()
	return S
print(generate_counts())
