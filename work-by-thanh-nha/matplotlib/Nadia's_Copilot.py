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

def parse_csv(file_name):
    """
    Parses a CSV file and returns a list of lists.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
        results = []
        for line in lines:
            fields = line.strip().split(',')
            results.append(Result(fields[0], fields[1], float(fields[2])))
        
    return results


def plot_cactus_broken(files, output):
    #-------------Original Code to Plot Data------------------------
    break_point = 10

    results = []    
    for file in files:
        res = parse_csv(file)
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
        xys1 = [xy for xy in xys if xy[0] < break_point]
        xys2 = [xy for xy in xys if xy[0] >= break_point]
        m = next(marker)
        ax1.plot(x, y, marker=m)
        ax2.plot([-100] + [xy[0] for xy in xys2], [xys1[len(xys1) - 1][1]] + [xy[1] for xy in xys2], marker=m)

    #----------------------------------------------------------------------------------------------------------


    #plot break point <= Natural Language Prompt For Copilot
    ax1.hlines(TOTAL_BENCH, 0, break_point, linestyles='dashed', color='gray', label="Total # of benchmarks")
    ax2.hlines(TOTAL_BENCH, break_point, TIMEOUT, linestyles='dashed', color='gray', label="Total # of benchmarks")
   
    #set limits on x axis <= Natural Language Prompt For Copilot
    ax1.set_xlim(0.001, break_point)
    ax2.set_xlim(break_point, TIMEOUT)
    ax1.set_ylabel("# Benchmarks Solved")
    ax2.legend(["CyclEgg", "CycleQ", "Total # of benchmarks"], loc="lower right")
   
    #add label for Time at the bottom for the whole plot  <= Natural Language Prompt For Copilot
    fig.text(0.5, 0.04, 'Time (s)', ha='center')

    #remove right boarderline of ax1                    <= Natural Language Prompt For Copilot
    ax1.spines.right.set_visible(False)
    #remove left boarderline of ax2                     <= Natural Language Prompt For Copilot
    ax2.spines.left.set_visible(False)


    #If fonttype = 1 doesn't work with LaTeX, try fonttype 42.  <= Natural Language Prompt For Copilot
    plt.rc('pdf',fonttype = 42)
    plt.rc('ps',fonttype = 42)
    
    plt.savefig(output)
    plt.close()

def run():
    parser = argparse.ArgumentParser(description='Plot the results of a simulation.')
    parser.add_argument('--files', nargs='+', help='The CSV file to plot.')
    parser.add_argument('--type', help='The type of plot to produce.', choices=['cactus', 'cactus-broken', 'scatter', 'aggregate', 'speedup'])
    parser.add_argument('--output', help='The output file to write.')
    
    args = parser.parse_args()


    if args.type == 'cactus-broken':
        plot_cactus_broken(args.files, args.output)

if __name__ == "__main__":
    run()