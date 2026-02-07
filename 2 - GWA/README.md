1. Which approach demonstrates true parallelism in Python? Explain.
    
    The **multiprocessing** approach demonstrates **true parallelism** because it bypasses Python’s **Global Interpreter Lock (GIL)**. When I input the 5 grades (`1.75`, `1.00`, `1.50`, `2.00`, `1.25`) into the `gwa_multiprocessing.py` script, each process ran in its own memory space with its own instance of the Python interpreter. This allows the operating system to assign each process to a **different CPU core** to run the calculation at the exact same time.

    In contrast, the **multithreading** approach only demonstrates **concurrency**. Even though I split the same 5 grades across multiple threads, the GIL ensures that only **one thread** can execute Python bytecode at any given moment. This means the threads are just switching back and forth on a single core rather than running simultaneously.

    ### Observations from the execution:

    * The multiprocessing output shows different **Process IDs** (PIDs like `18176` and `25860`), proving that the tasks handling the 5 grades are running as independent entities that do not share the GIL.
    * Only **multiprocessing** can utilize multiple CPU cores for CPU-bound tasks like calculating GWA. Multithreading is stuck using only **one core** regardless of the input size.
    * The higher execution time in the multiprocessing output (**209.92 ms**) is due to the time it takes the OS to set up separate memory spaces. Multithreading is "faster" (**1.97 ms**) for this small dataset of 5 grades because threads share the same memory and start up quickly, but they still aren't running in parallel.
    * The multithreading code requires a `threading.Lock()` to prevent threads from interfering with the shared list of grades, which further proves they are **competing for the same resources** rather than working independently.

2. Compare execution times between multithreading and multiprocessing.

   In our execution, the **multithreading** approach was significantly faster, completing in `1.97 ms`, while the **multiprocessing** approach took `209.92 ms`. This result happens because creating a new process is a **"heavy"** operation for the operating system. When we ran the multiprocessing script, the computer had to allocate separate memory and start a new instance of Python for each of the three processes. For a small task like calculating the average of just 5 grades, the time spent setting up these processes took much longer than the actual math.
   
   In contrast, threads are **lightweight** and share the same memory, so they started almost instantly. However, if we were processing a large number of grades, the **multiprocessing** approach would eventually become faster because the three processes could run on different CPU cores at the same time.

3. Can Python handle true parallelism using threads? Why or why not?

    Based on our findings, **no**, Python cannot handle true parallelism using threads. The reason is the **Global Interpreter Lock (GIL)**. The GIL is a rule within Python that forces the interpreter to execute only **one thread** at a time, even if our computer has multiple CPU cores available.
    
    In our `multithreading.py` code, even though we created three threads to process the grades, they were not running at the exact same instant. Instead, they were **concurrent**, meaning the CPU was just switching between them incredibly fast. It gives the illusion of parallelism, but in reality, they are just taking turns using a single core. To achieve **true parallelism** where tasks run simultaneously on different cores, we had to use the **multiprocessing** approach instead.

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

    **Note:** We only tested **150 grades** for this test case scenario because VS Code crashed when attempting runs with larger, repeated inputs. Based on theory and typical Python behavior, if we scaled to **~1000 grades**, **multiprocessing** would generally be faster than multithreading for this CPU‑bound task, since it achieves true parallelism across multiple CPU cores, while multithreading is limited by the Global Interpreter Lock (GIL) and can add overhead as workload grows.

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
    
    **Multiprocessing** is better for **CPU-bound tasks** because it can run multiple processes in parallel across different CPU cores, bypassing Python’s Global Interpreter Lock (GIL).

    **Multithreading** is better for **I/O-bound tasks** because threads can run concurrently while waiting for external operations (like file access, network requests, or database queries), and the GIL does not significantly affect performance.

6. How did your group apply creative coding or algorithmic solutions in this lab?
   
    To handle grade computations more effectively, our group used unique coding and algorithmic methods that included both multithreading and multiprocessing techniques. We investigated how each method performed with increasing input sizes and utilised timing measurements to compare the results. During this process, we discovered the limitations of multithreading owing to the Global Interpreter Lock (GIL) and how multiprocessing accomplishes real parallel execution across many CPU cores. We optimized the program's execution through experimentation, comparing performance findings, and understanding why multiprocessing is faster for CPU-bound tasks, demonstrating algorithmic thinking.

## Execution Comparison

## Execution Comparison (GWA Computation)

| Method           | No. of Grades Input | Execution Order                          | GWA Output | Execution Time (ms)                   |
|------------------|---------------------|------------------------------------------|------------|---------------------------------------|
| Multithreading   |         5           | Concurrent thread execution (interleaved)|     1.50   |     1.97 ms                           |
| Multiprocessing  |         5           | Parallel process execution               |     1.50   |     209.92 ms                         |
| Multithreading   |         150         | Concurrent thread execution (interleaved)|      2     |     175.31 ms                         |
| Multiprocessing  |         150         | Parallel process execution               |      2     |     2.895200000011755ms               |

