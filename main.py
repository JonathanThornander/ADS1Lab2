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

def main():
    load = 0 # Used to display load indicator for user

    datagenerators = [UnsortedData, SortedData, AlmostSortedData, ReversedData]
    algorithms = [Mergesort, Bubblesort, Cocktailsort, QuickSort, SelectionSort, Insertionsort]

    maxsize = 600  # Bör ej vara mer än 1000 pga rekursicva algoritmer

    print("Starting...")
    for datagenerator in datagenerators:

        results = run(algorithms = algorithms, datagenerator = datagenerator, maxsize = maxsize, repeat = 10, step = 100)
        visualizer.plot_results(results, datagenerator.name)

        load += 1/len(datagenerators)
        print(f"{load*100} % done...")

    visualizer.show()
    

if __name__ == "__main__":
    main()