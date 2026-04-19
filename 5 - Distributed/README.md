**DEMO GIF**

![Demo](Assets/Demo.gif)

**Reflection Questions:**

1. How did you distribute orders among worker processes?
  
    Orders were distributed using MPI message passing in a master–worker model. The master process (rank 0) assigned orders to worker processes using a round‑robin approach, ensuring that tasks were spread evenly. Each worker received tasks through MPI.send() and processed them independently.

2. What happens if there are more orders than workers?
   
   When there are more orders than available workers, some workers process multiple orders. Because the master distributes tasks in a round‑robin manner, additional orders are reassigned to available workers, helping maintain balanced workload distribution across processes.

3. How did processing delays affect the order completion?
    
   Processing delays caused orders to complete in different and unpredictable sequences. Each worker introduced a random delay using time.sleep(), which simulated real processing time. As a result, tasks finished out of order, demonstrating concurrent execution and independent worker behavior.

4. How did you implement shared memory, and where was it initialized?

   Shared memory was implemented in a separate Python file using Python’s multiprocessing.Manager().list(). The shared list was initialized in the main process before spawning worker processes, allowing all workers to append their processed results to the same shared data structure.

5. What issues occurred when multiple workers wrote to shared memory simultaneously?

    When multiple worker processes wrote to the shared list without synchronization, inconsistencies could occur due to concurrent access. This demonstrated a race condition where operations on shared memory were not always performed safely or in a consistent order.

6. How did you ensure consistent results when using multiple processes?

    Consistency was ensured by using a Lock() to control access to the shared memory. By placing write operations inside a critical section protected by the lock, only one worker could modify the shared list at a time. This prevented race conditions and ensured that the final output contained a complete and consistent set of processed orders.