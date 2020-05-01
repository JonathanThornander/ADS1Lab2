import multiprocessing

import visualizer
from experiment_runner import run

from datastructures import arraymap, balanced_search_tree, binary_search_tree, hashtable, mrtree
from datagenerators import *

import sys
sys.setrecursionlimit(10**6) 

datagenerators = [RandomData, SortedData] # A list containing datagenerators, used to generate arrays of integers (i.e sorted, almost sorted, etc)
datastructures = [mrtree.Map, binary_search_tree.Map, balanced_search_tree.Map, arraymap.Map, hashtable.Map] # A list containing algorithms
maxsize = 1000  # Maximum list size. Can be hard on memory if to high when using recursive algorithms
step = 10  # Decides how much the list size will vary for every iteration. Low value = High Accuracy
repeat = 1

def main():
    print("Starting collecting data...")
    for datastructure in datastructures:
        p = multiprocessing.Process(target=execute, args=(datastructure,))
        p.start()
        #execute(datastructure)

def execute(datastructure):
    results = run(datastructure=datastructure, datagenerators=datagenerators, maxsize=maxsize, step=step, repeat=repeat)
    
    visualizer.plot_results(results, datastructure.name)

    print(f"Done calculating {datastructure.name}")
    visualizer.show()

if __name__ == "__main__":
    main()
