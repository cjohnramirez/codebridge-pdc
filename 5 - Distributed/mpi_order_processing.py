from mpi4py import MPI
from multiprocessing import Manager, Lock
import time
import random

def main():
    # MPI setup
    cb = MPI.COMM_WORLD
    rank = cb.Get_rank()
    size = cb.Get_size()

    # Safety Check for minimum processes
    if size < 2:
        if rank == 0:
            print("ERROR: Run with at least 2 processes using mpiexec -n 4")
        return

    # Shared data structures
    manager = Manager()
    shared_orders = manager.list()
    lock = Lock()

    # Master process
    if rank == 0:
        print("\n===== DISTRIBUTED ORDER PROCESSING SYSTEM =====\n")

        # Generate 5–8 orders (7 total)
        orders = []
        for i in range(1, 8):
            orders.append({
                "id": i,
                "item": f"Item-{i}"
            })

        print("MASTER: Created orders:")
        for o in orders:
            print(o)

        print("\nMASTER: Distributing orders...\n")

        # Distribute orders
        for i, order in enumerate(orders):
            worker_rank = (i % (size - 1)) + 1
            cb.send(order, dest=worker_rank, tag=0)
            print(f"MASTER: Sent order {order['id']} to worker {worker_rank}")

        # Stop signals
        for i in range(1, size):
            cb.send(None, dest=i, tag=0)

        # Allow workers time to finish
        time.sleep(3)

        # Final results
        print("\n===== FINAL RESULTS =====")
        for order in shared_orders:
            print(order)

    # Worker Processes
    else:
        while True:
            order = cb.recv(source=0, tag=0)

            if order is None:
                print(f"WORKER {rank}: Shutting down")
                break

            print(f"WORKER {rank}: Processing order {order['id']} ({order['item']})")

            time.sleep(random.uniform(0.5, 2.0))

            print(f"WORKER {rank}: Finished order {order['id']}")

            # Critical section
            with lock:
                shared_orders.append({
                    "order_id": order["id"],
                    "item": order["item"],
                    "processed_by": rank
                })

# Run the main function
if __name__ == "__main__":
    main()