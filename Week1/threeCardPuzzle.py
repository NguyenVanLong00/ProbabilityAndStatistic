red_bck="\x1b[41m%s\x1b[0m"
blue_bck="\x1b[44m%s\x1b[0m"
red=red_bck%'R'
black=blue_bck%'B'
Cards=[(red,black),(red,red),(black,black)]
counts={'same':0,'different':0}
from random import random

for j in range(50):
	i=int(random()*3.) # Select a random card
	side=int(random()*2.)
	C=Cards[i]
	if(side==1): # select which side to be "up"
		C=(C[1],C[0])
	same= 'same' if C[0]==C[1] else 'different' # count the number of times the two sides are the same or different.
	counts[same]+=1
	print(''.join(C)+' %-9s'%same, end='')
	if (j+1)%5==0:
		print()
print()
print(counts)