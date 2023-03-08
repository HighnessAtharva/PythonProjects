from multiprocessing import Process, cpu_count
import time
import os

from threading import Thread


class MuchCPU(Thread):
    def run(self):
        print(os.getpid())


if __name__ == "__main__":
    procs = [MuchCPU() for _ in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(f"work took {time.time() - t} seconds")

