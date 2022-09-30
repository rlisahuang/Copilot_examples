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
    for file in files:
        res = parseCVS(file)
        results.append(res)

    # plot core data
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    fig.subplots_adjust(wspace=0.05)  # adjust space between axes

    marker = itertools.cycle(('^', 'x', 'o', '+', 'v'))
    for tool_result in results:
        times = [r.time for r in tool_result if r.outcome == 'Valid']        
        y = [i for i in range(1, len(times) + 1)] + [len(times)]
        x = sorted(times) + [10000]
        xys = list(zip(x, y))
        xys1 = [xy for xy in xys if xy[0] < bp]
        xys2 = [xy for xy in xys if xy[0] >= bp]
        m = next(marker)
        ax1.plot(x, y, marker=m)
        ax2.plot([-100] + [xy[0] for xy in xys2],
         [xys1[len(xys1) - 1][1]] + [xy[1] for xy in xys2], marker=m)

    #axs1 x-axis to go from 0 to bp
    ax1.set_xlim(0, bp)
    #axs2 x-axis to go from bp to Timeout
    ax2.set_xlim(bp, TIMEOUT)

    #add x-axis label Time(s) at the bottom
    fig.text(0.5, 0.04, 'Time(s)', ha='center', va='center')

    #create limit lines for the two axes; limit is the TOTAL_BENCH
    #linestyle is a dotted line
    #line is light gray
    ax1.axhline(y=TOTAL_BENCH, color='lightgray', linestyle='dotted')
    ax2.axhline(y=TOTAL_BENCH, color='lightgray', linestyle='dotted')

    #add y-axis label "# Benchmarks Solved" at the left of ax1
    fig.text(0.04, 0.5, '# Benchmarks Solved', ha='center', va='center',
        rotation='vertical')

    #set y ticks for ax1 by 5
    ax1.set_yticks(range(0, TOTAL_BENCH + 1, 5))
    #set y ticks for ax2 by 5 and place on right hand side
    ax2.set_yticks(range(0, TOTAL_BENCH + 1, 5))
    ax2.yaxis.tick_right()
    #show y numbers on ax2
    ax2.yaxis.set_label_position("right")
    #set y ticks for ax2 to be the same as ax1
    ax2.set_yticklabels(ax1.get_yticklabels())
    

    #make right line of ax1 invisible
    ax1.spines['right'].set_visible(False)
    #make left line of ax2 invisible
    ax2.spines['left'].set_visible(False)

    #create legend in lower left of ax2: "CyclEgg", "CycleQ", "Total Benchmarks"
    ax2.legend(["CyclEgg", "CycleQ", "Total Benchmarks"], loc='lower left')







    
    

   


    


    

    



filename1 = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\cycleq.csv"
filename2 = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\results.csv"
files = [filename1, filename2]
output = "C:\\Users\\tumit\\OneDrive\\Documents\\copilot\\examplePB.py\\bla.pdf"
plotCactusBroken(files, output)

