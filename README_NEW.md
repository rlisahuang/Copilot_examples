### Data Science (data_sci.py)
1. Send a query to some API to obtain some data
2. Grab the first ten data points from the response, both for the x and the y axes
-- limitations: bad support for large quantities of data
3. Plot the data
4. Notice that the labels on the x axis are too long. 
5. Go back to step 2 to shorten the data neede for the x axis labels.


### matplotlib (barlabels.py)
1. Given some short, raw data, plot them
2. Make modifications to the plot

### string manipulation (type_conversion.py)
... without using int() and str() ...
1. convert string representations of integers to their int values
2. convert integers to their string representations


### next step: data frames! (less than 10 rows is good)


### General Notes
1. importing external libraries has this general problem of being too slow --> preventing PB from showing up
2. you cannot put `plot()` at the end of the code; otherwise a plot will pop up automatically
3. some API has limitations on the number of requests permitted in one minute, causing live programming to fail
