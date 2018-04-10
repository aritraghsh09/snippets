##############################
#	curvefit.py
#	Python Routine to fit a function to some data using Scipy's curvefit.
#
#	Aritra Ghosh
#############################

import numpy as np
import math
import pylab as plt
from scipy.optimize import curve_fit

#define a function to fit
def func(x, a, b):
	return a*np.sin(2*x)+b

#reading in the data
data = plt.genfromtxt("work.txt",names=True)
x_rad = (data["theta"]*math.pi)/180

#fit the data and store the optimized parameters and covariances in two arrays. 
popt,pcov = curve_fit(func,x_rad,data["V"])
perr = np.sqrt(np.diag(pcov))

#Generating points using the fitted function
x_fit = np.linspace(45,90,200)
x_fit_rad = (x_fit*math.pi)/180
y_fit = func(x_fit_rad,popt[0],popt[1]) 

#Plot data and fit to it
plt.scatter(data["theta"],data["V"],label="Data")
plt.plot(x_fit,y_fit,label="Fit",color="r")


#Modify plot
plt.xlabel("$\\theta$")
plt.title("Variation of Visibility (V) with angle of Polarizer 2 to the horizontal ($\\theta$)\n\n")
plt.ylabel("Visibility (in$\%$)")
plt.legend(loc="best")
plt.savefig("fit.png")

#Print Results
print popt
print pcov
print perr
