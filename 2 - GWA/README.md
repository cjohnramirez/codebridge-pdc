1. Which approach demonstrates true parallelism in Python? Explain.

2. Compare execution times between multithreading and multiprocessing.

3. Can Python handle true parallelism using threads? Why or why not?

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

    **When the number of grades exceeds 1000, multiprocessing becomes the fastest method since it allows real parallel execution across many CPU cores while avoiding the Global Interpreter Lock. Multithreading, on the other hand, has no substantial improvement in speed for this CPU-bound activity and may even increase overhead.**

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
    
    **Multiprocessing** is better for **CPU-bound tasks** because it can run multiple processes in parallel across different CPU cores, bypassing Python’s Global Interpreter Lock (GIL).

    **Multithreading** is better for **I/O-bound tasks** because threads can run concurrently while waiting for external operations (like file access, network requests, or database queries), and the GIL does not significantly affect performance.

6. How did your group apply creative coding or algorithmic solutions in this lab?
   
    **To handle grade computations more effectively, our group used unique coding and algorithmic methods that included both multithreading and multiprocessing techniques. We investigated how each method performed with increasing input sizes and utilised timing measurements to compare the results. During this process, we discovered the limitations of multithreading owing to the Global Interpreter Lock (GIL) and how multiprocessing accomplishes real parallel execution across many CPU cores. We optimized the program's execution through experimentation, comparing performance findings, and understanding why multiprocessing is faster for CPU-bound tasks, demonstrating algorithmic thinking.**

## Execution Comparison

## Execution Comparison (GWA Computation)

| Method           | No. of Grades Input | Execution Order                          | GWA Output | Execution Time (ms)|
|------------------|---------------------|------------------------------------------|------------|--------------------|
| Multithreading   |         1000        | Concurrent thread execution (interleaved)|            |                    |
| Multiprocessing  |         1000        | Parallel process execution               |            |                    |

