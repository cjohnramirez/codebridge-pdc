from mpi4py import MPI
import time
import random


def main():
    CB = MPI.COMM_WORLD
    rank = CB.Get_rank()
    size = CB.Get_size()

    if size < 2:
        if rank == 0:
            print("Run this program with at least 2 processes using mpirun.")
        return

    # MASTER PROCESS
    if rank == 0:
        orders = [
            {"id": i, "item": f"Item-{i}"}
            for i in range(1, 8)
        ]

        print("\nMASTER: Created orders")
        for o in orders:
            print(o)

        print("\nMASTER: Distributing orders...\n")

        worker = 1
        for order in orders:
            CB.send(order, dest=worker, tag=0)
            print(f"MASTER: Sent order {order['id']} to worker {worker}")

            worker += 1
            if worker >= size:
                worker = 1

        # send exit signals
        for w in range(1, size):
            CB.send(None, dest=w, tag=0)

    # WORKER PROCESSES
    else:
        while True:
            task = CB.recv(source=0, tag=0)

            if task is None:
                print(f"Worker {rank}: exiting")
                break

            print(f"Worker {rank}: processing order {task['id']}")
            time.sleep(random.uniform(0.5, 2.0))
            print(f"Worker {rank}: finished order {task['id']}")


if __name__ == "__main__":
    main()