import time

def run(algorithms, datagenerator, maxsize, repeat = 1, step = 100):
    # algorithms = A list of algorithms
    # arrays = a list of lists containing integers to be sorted
    # repeat = how many times each algorithm should sort a specific list, used for better avarage
    results = {'n': [], 'algorithms': {}}

    for algorithm in algorithms:
        results['algorithms'][algorithm.name] = {}
        results['algorithms'][algorithm.name]['n_ops'] = []
        results['algorithms'][algorithm.name]['time'] = []

    for currentSize in range(1, maxsize, step):
        results[currentSize] = {}
        results['n'].append(currentSize)

        for algorithm in algorithms:
            algorithm = algorithm()  # instantiate a new algorithm-incatnce

            # Test Start
            starttime = time.time()
            for test in range(repeat):
                algorithm.sort(datagenerator.data(currentSize))
            endtime = time.time()
            # Test End

            results['algorithms'][algorithm.name]['n_ops'].append((algorithm.n_ops) / repeat)
            results['algorithms'][algorithm.name]['time'].append((endtime - starttime) / repeat)
        
    return results
