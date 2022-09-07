'''
Command:
python .\Nadia's_Original.py --files .\results.csv .\cycleq.csv --type cactus-broken --output bla.pdf
'''
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

def aggregate_results(files, output):
    results = []
    for file in files:
        res = parse_csv(file)
        results.append(res)

    num_files = len(results)
    aggregated = []
    for i in range(len(results[0])):
        aggregated.append(Result(results[0][i].name, results[0][i].outcome, results[0][i].time / num_files))
        for j in range(1, len(results)):
            aggregated[i].time += results[j][i].time / num_files

    with open(output, 'w') as file:
        for r in aggregated:
            file.write(f'{r.name},{r.outcome},{r.time}\n')

def compute_speedups(files, output):
    results = []
    for file in files:
        res = parse_csv(file)
        results.append(res)

    speedups = []
    for x in results[0]:
      for y in results[1]:
        if x.name == y.name and x.outcome == 'Valid' and y.outcome == 'Valid':
          speedups.append((x.name, y.time / x.time))

    # write to file
    with open(output, 'w') as file:
        for s in speedups:
            file.write(f'{s[0]},{s[1]}\n')

        file.write(f'{"min", min([s[1] for s in speedups])}\n')
        file.write(f'{"max", max([s[1] for s in speedups])}\n')
        file.write(f'{"geomean", geometric_mean([s[1] for s in speedups])}\n')


def plot_cactus(files, output):
    # assert len(files) % 3 == 0, 'Number of files must be a multiple of 3.'

    results = []
    for file in files:
        res = parse_csv(file)
        results.append(res)

    marker = itertools.cycle(('^', 'x', 'o', '+', 'v'))
    for tool_result in results:
        times = [r.time for r in tool_result if r.outcome == 'Valid']        
        y = [i for i in range(1, len(times) + 1)] + [len(times)]
        x = sorted(times) + [10000]
        m = next(marker)
        plt.plot(x, y, marker=m)
        plt.plot([], [], label='_nolegend_')

    plt.hlines(TOTAL_BENCH, 0, TIMEOUT, linestyles='dashed', color='gray', label="Total # of benchmarks")
    plt.xlim(0.001, TIMEOUT)
    plt.ylim(0, 80)
    plt.yticks(range(0, 80, 5))
    plt.legend(["CyclEgg", "CycleQ", "Total # of benchmarks"], loc="lower right")
    plt.xlabel("Time (s)")
    plt.ylabel("# Benchmarks Solved")


    #If fonttype = 1 doesn't work with LaTeX, try fonttype 42.
    plt.rc('pdf',fonttype = 42)
    plt.rc('ps',fonttype = 42)
    
    plt.savefig(output)
    plt.close()

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

    ax1.set_xlim(0, break_point)
    ax2.set_xlim(break_point, TIMEOUT)
    ax1.set_ylim(0, 80)

    ax1.hlines(TOTAL_BENCH, 0, TIMEOUT, linestyles='dashed', color='gray', label="Total # of benchmarks")
    ax2.hlines(TOTAL_BENCH, 0, TIMEOUT, linestyles='dashed', color='gray', label="Total # of benchmarks")
    plt.yticks(range(0, 80, 5))
    ax2.legend(["CyclEgg", "CycleQ", "Total # of benchmarks"], loc="lower right")
    fig.text(0.5,0.04, "Time (s)", ha='center', va='center')
    ax1.set_ylabel("# Benchmarks Solved")

    # set border lines
    ax1.spines.right.set_visible(False)
    ax2.spines.left.set_visible(False)
    ax1.yaxis.tick_left()
    ax2.yaxis.tick_right()
    ax2.tick_params(labelright=True)

    plt.rc('pdf',fonttype = 42)
    plt.rc('ps',fonttype = 42)
    
    plt.savefig(output)
    plt.close()

def process_scatter_data(files):
    results = []
    for file in files:
        res = parse_csv(file)
        results.append(res)

    xs, ys = [], []
    for x in results[0]:
      for y in results[1]:
        if x.name == y.name and x.outcome == 'Valid' and y.outcome == 'Valid':
          xs.append(x.time)
          ys.append(y.time)

    return xs, ys

def plot_scatter(files, output):
    x, y = process_scatter_data(files)

    # plt.figure(figsize=(4,5))
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(x, y)
    plt.plot([0, TIMEOUT], [0, TIMEOUT], 'k--')
    plt.xlim(0.01, TIMEOUT)
    plt.ylim(0.01, TIMEOUT)
    plt.xlabel("CyclEgg Time (s)")
    plt.ylabel("CycleQ Time (s)")

    #If fonttype = 1 doesn't work with LaTeX, try fonttype 42.
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

  

    if args.type == 'cactus':
        plot_cactus(args.files, args.output)
    elif args.type == 'cactus-broken':
        plot_cactus_broken(args.files, args.output)
    elif args.type == 'scatter':
        plot_scatter(args.files, args.output)
    elif args.type == 'aggregate':
        aggregate_results(args.files, args.output)
    elif args.type == 'speedup':
        compute_speedups(args.files, args.output)


if __name__ == "__main__":
    run()