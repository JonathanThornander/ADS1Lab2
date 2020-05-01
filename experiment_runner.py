import time

def run(datastructure, datagenerators, maxsize, step = 100, repeat = 10):
    results = {'n': [], 'datatype': {}}

    for datatype in datagenerators:
        results['datatype'][datatype.name] = {}
        results['datatype'][datatype.name]['Put'] = []
        results['datatype'][datatype.name]['Get'] = []
        results['datatype'][datatype.name]['Contains'] = []
        results['datatype'][datatype.name]['Delete'] = []

    for currentSize in range(step, maxsize, step):
        results['n'].append(currentSize)

        total_time_put = 0
        total_time_get = 0
        total_time_contains = 0
        total_time_delete = 0

        
        for datatype in datagenerators:
            for _ in range(repeat):
                list_of_kv_pairs = datatype.data(currentSize) # Initiates a new sequence of kv-pairs
                datastructure_obj = datastructure(currentSize)  # Initiates a new datastructure-instance

                # Put Test Start
                starttime = time.time()
                for kv_pair in list_of_kv_pairs:
                    datastructure_obj.put(kv_pair[0], kv_pair[1])
                total_time_put += time.time() - starttime
                
                # Put Test End

                # Get Test Start
                starttime = time.time()
                for kv_pair in list_of_kv_pairs:
                    datastructure_obj.get(kv_pair[0])
                total_time_get += time.time() - starttime
                # Get Test End

                # Contains Test Start
                starttime = time.time()
                for kv_pair in list_of_kv_pairs:
                    datastructure_obj.contains(kv_pair[0])
                total_time_contains += time.time() - starttime
                # Contains Test End

                # Delete Test Start
                starttime = time.time()
                for kv_pair in list_of_kv_pairs:
                    datastructure_obj.delete(kv_pair[0])
                total_time_delete += time.time() - starttime
                # Delete Test End

                del datastructure_obj

            results['datatype'][datatype.name]['Put'].append(total_time_put/repeat)
            results['datatype'][datatype.name]['Get'].append(total_time_get/repeat)
            results['datatype'][datatype.name]['Contains'].append(total_time_contains/repeat)
            results['datatype'][datatype.name]['Delete'].append(total_time_delete/repeat)

    return results
