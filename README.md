### matplotlib (barlabels.py)
1. Given some short, raw data, plot them
2. Make modifications to the plot (e.g., adding labels to the bars)

### string manipulation (type_conversion.py)
... without using int() and str(), or recursions ...
Idea 1:
1. Convert string representations of integers to their int values
Idea 2:
1. Convert integers to their string representations


### data frames (data_frames.py)
1. Given a list of row names, generate the same number of random values
2. Convert the existing data into a data frame
3. Repeat the steps above to generate another data frame (with some different row names)
4. Merge the two data frames without dropping any values
5. Based on the result, decide which values to keep by merging columns / dropping values
6. Create a new column in which the values are computed based on values from another column
7. Drop rows based on some constraint


### data science (data_sci.py)
1. Send a query to some API to obtain some data
2. Grab the first ten data points from the response, both for the x and the y axes
3. Plot the data
4. Notice that the labels on the x axis are too long. 
5. Go back to step 2 to shorten the data neede for the x axis labels.
-- limitations bad support for large quantities of data



### general notes
1. Importing external libraries has a general problem of slowing down the computation --> preventing PB from showing up
2. You cannot put `plot()` at the end of the code; otherwise a plot will pop up automatically
3. Some API has limitations on the number of requests permitted in one minute, causing live programming to fail
4. Data frames should be limited to 2-3 columns and 10 
5. Visualizing loops with data frames / plots are a bit overwhelming
