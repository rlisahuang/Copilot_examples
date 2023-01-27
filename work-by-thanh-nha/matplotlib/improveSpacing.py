'''
StackOverFlow:
https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots

How to improve subplot size/spacing with many subplots?
'''
#-----------Example Code From Comments-------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# sinusoidal sample data
sample_length = range(1, 15+1)
rads = np.arange(0, 2*np.pi, 0.01)
data = np.array([np.sin(t*rads) for t in sample_length])
df = pd.DataFrame(data.T, index=pd.Series(rads.tolist(), name='radians'), columns=[f'freq: {i}x' for i in sample_length])

# display(df.head(3))
#freq: 1x  freq: 2x  freq: 3x  freq: 4x  freq: 5x  freq: 6x  freq: 7x  freq: 8x  freq: 9x  freq: 10x  freq: 11x  freq: 12x  freq: 13x  freq: 14x  freq: 15x
#radians                                                                                                                                                            
#0.00     0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000   0.000000   0.000000   0.000000   0.000000   0.000000   0.000000
#0.01     0.010000  0.019999  0.029996  0.039989  0.049979  0.059964  0.069943  0.079915  0.089879   0.099833   0.109778   0.119712   0.129634   0.139543   0.149438
#0.02     0.019999  0.039989  0.059964  0.079915  0.099833  0.119712  0.139543  0.159318  0.179030   0.198669   0.218230   0.237703   0.257081   0.276356   0.295520

# default plot with subplots; each column is a subplot
axes = df.plot(subplots=True)

#------------------------------------------------------------


#stop subplots from overlapping <= Natural Language Prompt For Copilot
plt.tight_layout()

#stop x_axis and y_axisfrom overlapping   <= Natural Language Prompt For Copilot
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()