'''
StackOverFlow: 
https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots

Most Frequently Asked Question
How to plot in multiple subplots?

'''
import matplotlib.pyplot as plt 

#Given sample data
x = range(10)
y = range(10)

#how to plot in multiple subplots <= Natutal Language Prompt For Copilot
fig, axs = plt.subplots(2, 2)
#plt.show() <= Comment to immitate PB
axs[0, 0].plot(x, y)
#plt.show() <= Comment to immitate PB
axs[0, 1].plot(x, y)
#plt.show() <= Comment to immitate PB
axs[1, 0].plot(x, y)
#plt.show() <= Comment to immitate PB
axs[1, 1].plot(x, y)
plt.show()