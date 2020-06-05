import itertools 
from itertools import product


#Write the function complement_of_union that first determines  
#𝐴∪𝐵  and then evaluates the complement of this set. Output the 
#tuple:  (𝐴∪𝐵,(𝐴∪𝐵)𝑐) .

#my solution here
def complement_of_union(A,B,U):
	unionSet = set.union(A,B)
	negationOfunionset = U.difference(unionSet)
	result = (unionSet,negationOfunionset)

	return result



#check
A={1,2,3}
B={3,-6,2,-0}
U={-10,-9,-8,-7,-6,0,1,2,3,4}

print(complement_of_union(A,B,U))
# output must be: ({-6, 0, 1, 2, 3}, {-10, -9, -8, -7, 4})



#Write the function intersection_of_complements that first 
#determines  𝐴𝑐  and  𝐵𝑐  and then evaluates the 
#intersection of their complements. Output the tuple:  (𝐴𝑐,𝐴𝑐∩𝐵𝑐)

def intersection_of_complements(A,B,U):
	negationOfA = U.difference(A)
	negationOfB = U.difference(B)

	result = (negationOfA,set.intersection(negationOfA,negationOfB))
	return result

print(intersection_of_complements(A,B,U))
