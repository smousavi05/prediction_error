# prediction error calculator 

To calculate the moving average between the actual values and the predictions:

1 - first we build  a dictionary for predicted prices for each hour.stock pair
2 - read the actual prices line by line and for each hour.stock pair 
3 - if the predicted price for the current hour.stock pair exist then calculate the error and keep it in cash 
4 - calculate the average errors for each hour and save it in a new variable (av)
5 - read the window size from input.
6 - use a generator to generate the moving windows of the desired size.
7 - calculate the average errors for each window and write it into the output file.

This code just use itertools package for generating the moving windows
This makes it fast for large input file sizes.

The relative paths to the input files and the output directory has been 
predefined in the code so there is no need for argument passing. 

Run instruction:

`./run.sh` 
