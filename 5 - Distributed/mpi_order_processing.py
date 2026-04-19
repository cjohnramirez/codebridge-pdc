from mpi4py import MPI
import time
import random


def run():
    CB = MPI.COMM_WORLD
    pid = CB.Get_rank()
    total = CB.Get_size()

    if total < 2:
        if pid == 0:
            print("Need at least 2 MPI processes.")
        return

    if pid == 0:
        # create work
        orders = []
        for i in range(1, 8):
            orders.append({
                "id": i,
                "item": "Item-" + str(i)
            })

        print("\nMASTER process started")
        print("Orders to process:")
        for o in orders:
            print(o)

        # distribute work
        worker_index = 1
        for order in orders:
            CB.send(order, dest=worker_index, tag=0)
            print(f"Sent order {order['id']} to worker {worker_index}")

            worker_index += 1
            if worker_index >= total:
                worker_index = 1

        # notify workers to stop
        for w in range(1, total):
            CB.send(None, dest=w, tag=0)

        # receive results
        completed = []
        for _ in range(len(orders)):
            msg = CB.recv(source=MPI.ANY_SOURCE, tag=1)
            completed.append(msg)

        print("\nProcessing results:")
        for c in completed:
            print(c)

    else:
        while True:
            task = CB.recv(source=0, tag=0)

            if task is None:
                print(f"Worker {pid} exiting")
                break

            print(f"Worker {pid} working on order {task['id']}")
            time.sleep(random.uniform(0.5, 2.0))

            result = {
                "order_id": task["id"],
                "item": task["item"],
                "worker": pid
            }

            CB.send(result, dest=0, tag=1)


if __name__ == "__main__":
    run()