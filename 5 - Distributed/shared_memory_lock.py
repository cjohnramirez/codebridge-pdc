from multiprocessing import Process, Manager, Lock
import time
import random


def worker(order_id, shared_orders, lock, use_lock):
    time.sleep(random.uniform(0.5, 2.0))

    result = {
        "order_id": order_id,
        "processed_by": order_id
    }

    if use_lock:
        with lock:
            shared_orders.append(result)
    else:
        # intentionally unsafe
        shared_orders.append(result)

    print(f"Worker {order_id} finished")


if __name__ == "__main__":
    manager = Manager()
    shared_orders = manager.list()
    lock = Lock()

    # Toggle this to see the difference with and without locks
    use_lock = True

    processes = []

    for i in range(1, 8):
        p = Process(
            target=worker,
            args=(i, shared_orders, lock, use_lock)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\nFinal shared orders list:")
    for order in shared_orders:
        print(order)

    print("\nTotal completed orders:", len(shared_orders))