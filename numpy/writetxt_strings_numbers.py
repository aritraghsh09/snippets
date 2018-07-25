###########################################
#	writetxt_strings_numbers.py
#
#	Aritra Ghosh
#
#	Using genfromtxt or savetxt to read-in/write numbers and strings at the same time is not possible unless you have specifically made a structured array. This example shows how to do it.
###########################################

import numpy as np

para_1 = ["Hello","Blah","Blah"]
para_2 = [1,2,3,4]

stacked_para = np.zeros(len(para_1),dtype=[('Parameter 1',object), ('Parameter 2', np.int64)])
stacked_para["Parameter 1"] = para_1 
stacked_para["Parameter 2"] = para_2

out_file = open("file.txt","w")
np.savetxt(out_file,stacked_para,delimiter=" ",fmt=['%s','%d'])
out_file.close()
