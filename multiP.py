import os
import timeit
from multiprocessing import Process

import import_function

def start_processes():
    processes = []
    for i in range(os.cpu_count()):
        print("registering process %d" % i)
        processes.append(Process(target=import_function))
    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == "__main__":
    multi = "start_processes()"
    setup = """from __main__ import start_processes"""
    print("Z procesami: ", timeit.timeit(stmt=multi,
                                        setup = setup,
                                        number = 1))