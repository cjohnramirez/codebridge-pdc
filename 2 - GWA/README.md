1. Which approach demonstrates true parallelism in Python? Explain.

2. Compare execution times between multithreading and multiprocessing.

3. Can Python handle true parallelism using threads? Why or why not?

4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?
When the number of grades exceeds 1000, multiprocessing becomes the fastest method since it allows real parallel execution across many CPU cores while avoiding the Global Interpreter Lock. Multithreading, on the other hand, has no substantial improvement in speed for this CPU-bound activity and may even increase overhead.

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?

6. How did your group apply creative coding or algorithmic solutions in this
lab?

## Execution Comparison

## Execution Comparison (GWA Computation)

| Method           | No. of Grades Input | Execution Order | GWA Output | Execution Time (ms) |
|------------------|---------------------|----------------|------------|--------------------|
| Multithreading   |                     |                |            |                    |
| Multiprocessing  |                     |                |            |                    |

