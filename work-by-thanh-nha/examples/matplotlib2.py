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