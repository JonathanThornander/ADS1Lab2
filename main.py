import multiprocessing

import visualizer
from experiment_runner import run

from algorithms.selectionsort import SelectionSort
from algorithms.insertionsort import Insertionsort
from algorithms.quicksort import QuickSort
from algorithms.bubblesort import Bubblesort
from algorithms.cocktailsort import Cocktailsort
from algorithms.mergesort import Mergesort
from algorithms.bogosort import Bogosort
from datagenerators import *

datagenerators = [UnsortedData, SortedData, AlmostSortedData, ReversedData] # A list containing datagenerators, used to generate arrays of integers (i.e sorted, almost sorted, etc)
algorithms = [QuickSort, SelectionSort, Insertionsort] # A list containing algorithms
maxsize = 100  # Maximum list size. Should be lower than 2000 when using recursive algorithms
repeat = 20  # Controlls how many list that should be generated for a given lenght and type. Low value = Hight Accuracy
step = 10  # Controlls how much the list size will vary for every iteration. Low value = Hight Accuracy


def main():
    print("Starting collecting data...")
    for datagenerator in datagenerators:
        p = multiprocessing.Process(target=execute, args=(datagenerator,))
        p.start()

def execute(datagenerator):
    results = run(algorithms=algorithms, datagenerator=datagenerator, maxsize=maxsize, repeat=repeat, step=step)
    visualizer.plot_results(results, datagenerator.name)

    print(f"Done calculating {datagenerator.name}")
    visualizer.show()

if __name__ == "__main__":
    main()