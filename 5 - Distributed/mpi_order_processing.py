from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ---------------- SAFETY CHECK ----------------
if size < 2:
    if rank == 0:
        print("ERROR: Run with at least 2 processes using mpiexec -n 4")
    exit()

if rank == 0:

    print("\n===== DISTRIBUTED ORDER PROCESSING SYSTEM =====\n")

    # Generate 5–8 orders
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

    # Send orders to workers
    for i, order in enumerate(orders):
        worker_rank = (i % (size - 1)) + 1
        comm.send(order, dest=worker_rank, tag=0)
        print(f"MASTER: Sent order {order['id']} to worker {worker_rank}")

    # Send stop signals
    for i in range(1, size):
        comm.send(None, dest=i, tag=0)

else:
    while True:
        order = comm.recv(source=0, tag=0)

        if order is None:
            print(f"WORKER {rank}: Shutting down")
            break

        print(f"WORKER {rank}: Processing order {order['id']} ({order['item']})")

        # simulate processing delay
        time.sleep(random.uniform(0.5, 2.0))

        print(f"WORKER {rank}: Finished order {order['id']}")

        # send result back to master
        comm.send({
            "order_id": order["id"],
            "item": order["item"],
            "worker": rank
        }, dest=0, tag=1)