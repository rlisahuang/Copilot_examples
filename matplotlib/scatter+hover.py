'''
StackOverFlow:
https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot

How to add hovering annotations to a plot?
'''

#-------------------Generic Code Example---------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.rand(15)
y = np.random.rand(15)

#create scatter plot
plt.scatter(x, y)
#--------------------------------------------------------------

#when cursor hovers over point on graph, show value
#otherwise, do not show value                        <= Natural Language Prompt For Copilot
for i, j in zip(x, y):
    plt.annotate(str(j), xy=(i, j))

#copilot can not do this -> gives too simple of solutions

plt.show()  

