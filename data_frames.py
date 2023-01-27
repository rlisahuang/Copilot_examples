'''
Data Frame Operations.
## denotes non-prompt comments.
'''

import pandas as pd
import numpy as np

## control over randomness
np.random.seed(0)

# create a list of 4 random numbers rounded up to 2 decimals
## I converted the synth'd code into a function
def getFourNumbers():
    numbers = np.random.rand(4) * 100
    numbers = np.round(numbers, 2)
    return numbers

d1 = {
    'col1': ['A', 'B', 'D', 'E'],
    'col2': getFourNumbers()
}

# create a data frame from d1
df = pd.DataFrame(d1)

d2 = {
    'col1': ['B', 'E', 'C', 'D'],
    'col2': getFourNumbers()
}

## copied from the above
## create a data frame from d2
## Note: Ideally only show the data frames
df2 = pd.DataFrame(d2)

# join df1 and df2 on col1
## outer join is what I want
df_join = df.merge(df2, on='col1', how='outer')

# combine col2_x and col2_y in df_join by replacing NaN values with non-NaN values
## this looks like what I want: it arbitrarily replaces col2_x with col2_y when both values are not NaN
df_join['col2'] = df_join['col2_x'].combine_first(df_join['col2_y'])

# drop the columns that contain NaN values
## this looks good
df_join.dropna(axis=1, inplace=True)

## this is part of the solution, but looks good (no effects) so I'd keep it
# drop the rows that contain NaN values
df_join.dropna(axis=0, inplace=True)

# add col3 to df_join where the values are the average of all values in col2
## this looks good
df_join['col3'] = df_join['col2'].mean()


# remove rows from df_join if the values in col2 are less than the values in col3 (the average)
## A,C,E should be removed; so this looks good
df_join = df_join[df_join['col2'] > df_join['col3']]
