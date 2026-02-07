1. Which approach demonstrates true parallelism in Python? Explain.
    
    The **multiprocessing** approach demonstrates **true parallelism** because it bypasses Python’s **Global Interpreter Lock (GIL)**. When I input the 5 grades (`1.75`, `1.00`, `1.50`, `2.00`, `1.25`) into the `gwa_multiprocessing.py` script, each process ran in its own memory space with its own instance of the Python interpreter. This allows the operating system to assign each process to a **different CPU core** to run the calculation at the exact same time.

    In contrast, the **multithreading** approach only demonstrates **concurrency**. Even though I split the same 5 grades across multiple threads, the GIL ensures that only **one thread** can execute Python bytecode at any given moment. This means the threads are just switching back and forth on a single core rather than running simultaneously.

    ### Observations from the execution:

    * The multiprocessing output shows different **Process IDs** (PIDs like `18176` and `25860`), proving that the tasks handling the 5 grades are running as independent entities that do not share the GIL.
    * Only **multiprocessing** can utilize multiple CPU cores for CPU-bound tasks like calculating GWA. Multithreading is stuck using only **one core** regardless of the input size.
    * The higher execution time in the multiprocessing output (**209.92 ms**) is due to the time it takes the OS to set up separate memory spaces. Multithreading is "faster" (**1.97 ms**) for this small dataset of 5 grades because threads share the same memory and start up quickly, but they still aren't running in parallel.
    * The multithreading code requires a `threading.Lock()` to prevent threads from interfering with the shared list of grades, which further proves they are **competing for the same resources** rather than working independently.

2. Compare execution times between multithreading and multiprocessing.

3. Can Python handle true parallelism using threads? Why or why not?

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

    **Note:** We only tested **150 grades** for this test case scenario because VS Code crashed when attempting runs with larger, repeated inputs. Based on theory and typical Python behavior, if we scaled to **~1000 grades**, **multiprocessing** would generally be faster than multithreading for this CPU‑bound task, since it achieves true parallelism across multiple CPU cores, while multithreading is limited by the Global Interpreter Lock (GIL) and can add overhead as workload grows.

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
    
    **Multiprocessing** is better for **CPU-bound tasks** because it can run multiple processes in parallel across different CPU cores, bypassing Python’s Global Interpreter Lock (GIL).

    **Multithreading** is better for **I/O-bound tasks** because threads can run concurrently while waiting for external operations (like file access, network requests, or database queries), and the GIL does not significantly affect performance.

6. How did your group apply creative coding or algorithmic solutions in this lab?
   
    **To handle grade computations more effectively, our group used unique coding and algorithmic methods that included both multithreading and multiprocessing techniques. We investigated how each method performed with increasing input sizes and utilised timing measurements to compare the results. During this process, we discovered the limitations of multithreading owing to the Global Interpreter Lock (GIL) and how multiprocessing accomplishes real parallel execution across many CPU cores. We optimized the program's execution through experimentation, comparing performance findings, and understanding why multiprocessing is faster for CPU-bound tasks, demonstrating algorithmic thinking.**

## Execution Comparison

## Execution Comparison (GWA Computation)

| Method           | No. of Grades Input | Execution Order                          | GWA Output | Execution Time (ms)|
|------------------|---------------------|------------------------------------------|------------|--------------------|
| Multithreading   |         150         | Concurrent thread execution (interleaved)|            |                    |
| Multiprocessing  |         150         | Parallel process execution               |            |                    |

