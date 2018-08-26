#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:43:29 2018

This is for coding challenge of insight data engineering 

@author: mostafamousavi
"""
from itertools import islice

def sliding_windows(seq, n=2):
    ''' Returns a sliding window (of width n) over data '''
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

# constructing a dictionary for predictions 
predictions = {}
with open('../input/predicted.txt') as f:
    for line in f:
        line = str(line)
        l = line.split('|')                
        if len(l) == 3:
            predictions[l[0]+'.'+l[1]] = float(l[2])

cash = [0]
hrR = 1
av = []
t = []
# reading the actual values from the input file 
with open('../input/actual.txt') as f:
    for line in f:
        line = str(line)
        l = line.split('|')                
        hr = int(l[0]);
        hr_stock = l[0]+'.'+l[1]                       
        price_ac = l[2]
        # checking for the associated predition 
        if hr_stock in predictions:
            if hr == hrR:
                # puttin the calculated errors for each hour in cash 
                error = round(abs(float(price_ac) - predictions[hr_stock]), 2)
                cash.append(error)
            else:
                # calclulating the average error per hour 
                av.append(round(sum(cash)/len(cash), 2))               
                hrR = hr;
                cash = [];
                error = round(abs(float(price_ac) - predictions[hr_stock]), 2)
                cash.append(error)

# reading the window size from the input directory 
w  = open('../input/window.txt', 'r')
window = int(w.readlines()[0])
w.close()

text_out = open('../output/comparison.txt', "w")
# getting sliding windows from the hourly errors 
sldW = sliding_windows(av, window)
# calculating the moving windowed avarages and writing into the output file.
for i, wd in enumerate(sldW):  
    start = i + 1 
    end = start + 3
    text_out.write(str(start)+'|'+ str(end) +'|'+ str(round(sum(wd)/len(wd), 2))+'\n')
text_out.close()
        
