'''
StackOverFlow: 
Most Frequently Asked Question
How to plot in multiple subplots?

'''
import matplotlib.pyplot as plt 

#Given sample data
a = range(10)
b = range(10)

c = range(0,10,2)
d = range(0,10,2)

e = range(0,10,3)
f = range(0,10,3)

g = range(5,10)
h = range(5,10)

#Plot 4 different subplots
plt.subplot(2,2,1)
plt.plot(a,b, 'r')

plt.subplot(2,2,2)
plt.plot(c,d, 'b')

plt.subplot(2,2,3)
plt.plot(e,f, 'g')

plt.subplot(2,2,4)
plt.plot(g,h, 'y')



