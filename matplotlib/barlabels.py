'''
StackOverflow question:
https://stackoverflow.com/questions/28931224/how-to-add-value-labels-on-a-bar-chart
How to add value labels on a bar chart?
'''
#------Original Code Snippet From StackOverflow-----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [6, 16, 75, 160, 244, 260, 145, 73, 16, 4, 1]

# In my original code I create a series and run on that, 
# so for consistency I create a series from the list.
freq_series = pd.Series(frequencies)

x_labels = [108300.0, 110540.0, 112780.0, 115020.0, 117260.0, 119500.0, 
            121740.0, 123980.0, 126220.0, 128460.0, 130700.0]

# Plot the figure.
plt.figure(figsize=(12, 8))
fig = freq_series.plot(kind='bar')
fig.set_title('Amount Frequency')
fig.set_xlabel('Amount ($)')
fig.set_ylabel('Frequency')
fig.set_xticklabels(x_labels)
#----------------------------------------------------------

#add value labels ontop of the bars in the center of the bar <= Natural Language Prompt For Copilot
#Written by Copilot:
for i, v in enumerate(freq_series):
    fig.text(i, v, str(v), color='black', ha='center')

plt.show()

'''
Failed Examples That Copilot Wrote:
----------------------------------------------------------------
1. Nothing showed up on th eplot
#add value labels on the bars in the center of the bar <= Natutal Language Prompt For Copilot
#Written by Copilot:
for i in range(len(freq_series)):
    plt.text(x_labels[i], frequencies[i], frequencies[i], ha='center', va='bottom')
----------------------------------------------------------------

2. Labels are left justified not centered
#add value labels ontop of the bars in the center  <= Natural Language Prompt For Copilot
#Written by Copilot:
for i, v in enumerate(freq_series):
    fig.text(i, v, str(v))
----------------------------------------------------------------
'''

