import pylab as plt
import numpy as np
import sys
from matplotlib.legend_handler import HandlerBase 

#Complicated Label Handler for Handling labels.
class AnyObjectHandler(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        l1 = plt.Line2D([x0,y0+width], [0.7*height,0.7*height],
                           linestyle=orig_handle[0], color=orig_handle[1])
        l2 = plt.Line2D([x0,y0+width], [0.3*height,0.3*height], 
                           linestyle=orig_handle[2], color=orig_handle[3])
        return [l1, l2]


#Reading in data from files
data_1 = plt.genfromtxt("file1.txt",names=True)
data_2 = plt.genfromtxt("file2.txt",names=True)

#Putting read data into arrays
acc_1 = data_1["acc"]
val_acc_1 = data_1["val_acc"]
loss_1 = data_1["loss"]
epochs_1 = np.linspace(1,acc_1.size,acc_1.size)

acc_2 = data_2["acc"]
val_acc_2 = data_2["val_acc"]
loss_2 = data_2["loss"]
epochs_2 = np.linspace(1,acc_2.size,acc_2.size)

#initiating plot space
fig, ax1 = plt.subplots()

ax1.plot(epochs_1,val_acc_1,c='r')
ax1.plot(epochs_2,val_acc_2,c='r',ls='--')
#plt.xscale("Log")
#plt.yscale("Log")
ax1.set_xlabel("Epochs")
ax1.set_ylabel("Accuracy",color='r')
#ax1.set_ylim([0.6,1.0])
ax1.tick_params('y', colors='r')

#Creating a twin of the first plot
ax2 = ax1.twinx()
ax2.plot(epochs_1,loss_1,c='b')
ax2.plot(epochs_2,loss_2,c='b',ls='--')
ax2.set_ylabel("Loss",color='b')
ax2.tick_params('y', colors='b')


plt.legend([("-","r","-","b"), ("--","r","--","b")], ['Label 1', "Label 2"],
           handler_map={tuple: AnyObjectHandler()},loc='upper center', bbox_to_anchor=(0.5, 1.13),fancybox=True, shadow=True)
plt.show()



