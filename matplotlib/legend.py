'''
StackOverFlow:
https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot

How to put the legend outside the plot?
I have a series of 20 plots (not subplots) to be made in a single figure. 
I want the legend to be outside of the box. At the same time, 
I do not want to change the axes, as the size of the figure gets reduced.

I want to keep the legend box outside the plot area 
(I want the legend to be outside at the right side of the plot area).
Is there a way that I reduce the font size of the text inside the legend box, 
so that the size of the legend box will be small?
'''

import matplotlib.pyplot as plt
import numpy as np

#------Generic example taken from stackoverflow comment-----
x = np.arange(10)

fig = plt.figure()
ax = plt.subplot(111)

for i in range(5):
    ax.plot(x, i * x, label='$y = %ix$' % i)
#----------------------------------------------------------


#create legend outside of the plot area <= Natutal Language Prompt For Copilot
#Written by Copilot:
leg = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#reduce the font size of the text inside the legend box <= Natutal Language Prompt For Copilot
#Written by Copilot:
for label in leg.get_texts():
    label.set_fontsize('small')
plt.show()
