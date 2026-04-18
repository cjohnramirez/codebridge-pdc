Project Overview

This project explores the differences between sequential and parallel algorithm execution by implementing and evaluating sorting and searching algorithms. Both approaches were tested under varying workloads to understand how execution time, overhead, and system resource utilization affect performance.
The project includes:

- Sequential Merge Sort
- Parallel Merge Sort
- Sequential Linear Search
- Parallel Linear Search

Performance was measured using different dataset sizes, and a special case input was included which is the "already sorted case" to further analyze algorithm behavior.

GIF DEMO:

![Demo](Assets/Demo.gif)

Individual Reflection: 

Jhey Gulde: 

I saw distinct distinctions between the sequential and parallel execution approaches in this exercise. While parallel algorithms needed careful coordination between several processes, sequential algorithms followed a single control flow and were simpler to build and think about. Compared to the sequential technique, parallel execution required additional complexity such job segmentation, inter-process communication, and synchronisation, which made implementation more challenging. 

Because sequential execution has less overhead, it consistently performed better on small datasets when performance was evaluated across dataset sizes. Any possible speedup for light workloads was overshadowed by the expense of process creation and communication in the parallel approach. However, the parallel merge sort started to demonstrate performance gains as the dataset size grew, especially at 100,000 and 1,000,000 items, suggesting that the computational demand was substantial enough to take use of several CPU cores. Ensuring accuracy when combining sorted subarrays and returning the right global index in parallel searching was one of the major implementation problems. 

Careful reasoning was needed to manage synchronization and coordinate outcomes from several processes in order to prevent race situations and inaccurate outputs. I learned more about the overhead of parallelism and the significance of striking a balance between computing work and coordination costs as a result of this exercise. In general, parallelism was advantageous for large datasets when overhead was dominated by workload, while it was superfluous and sometimes harmful for smaller datasets where sequential processing remained more efficient.