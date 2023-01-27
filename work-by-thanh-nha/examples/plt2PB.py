import argparse
import itertools
from statistics import geometric_mean
import matplotlib.pyplot as plt

TIMEOUT = 3600
TOTAL_BENCH = 76

class Result:
    def __init__(self, name, outcome, time):
        self.name = name
        self.outcome = outcome
        self.time = time


def parseCVS(file_name):
    """
    Parses a CSV file and returns a list of lists.
    """
    with open(file_name) as file:
        lines = file.readlines()
        results = []
        for line in lines:
            fields = line.strip().split(',')
            results.append(Result(fields[0], fields[1], float(fields[2])))
        
    return results

def plotCactusBroken(files, output):
    bp = 10
    results = []
    test = 0
    for file in files:
        res = parseCVS(file)
        results.append(res)

    s = "hello world"
    x = 2 

    



filename1 = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\cycleq.csv"
filename2 = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\results.csv"
files = [filename1, filename2]
output = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\bla.pdf"
plotCactusBroken(files, output)

