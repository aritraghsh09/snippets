# A Simple Python Script which implements a progress bar. 
# Inspired by a StackOverflow answer. Don't remember whcih one! 
#
# Aritra Ghosh


import time
NUM_ITER = 100000

for i in range(0,NUM_ITER):
	bar_width = 110
    	b = bar_width * i / NUM_ITER
    	l = bar_width - b
    	print '\r' + u"\u2588" * b + '-' * l,
