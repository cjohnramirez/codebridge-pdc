**Project Overview**

This project explores the differences between sequential and parallel algorithm execution by implementing and evaluating sorting and searching algorithms. Both approaches were tested under varying workloads to understand how execution time, overhead, and system resource utilization affect performance.

**The project includes:**

- Sequential Merge Sort
- Parallel Merge Sort
- Sequential Linear Search
- Parallel Linear Search

Performance was measured using different dataset sizes, and a special case input was included which is the "already sorted case" to further analyze algorithm behavior.

**GIF DEMO:**

![Demo](Assets/Demo.gif)

**Individual Reflections:** 

**Jhey Gulde:** 

I observed a clear differences between sequential and parallel execution in this exercise. Sequential algorithms were easier to design and understand since they follow a single flow, while parallel algorithms required more effort due to task division, communication, and synchronization between processes. In terms of performance, sequential execution worked better for small datasets because it has less overhead, whereas parallel execution only became beneficial with larger datasets like 100,000 or 1,000,000 items, where multiple CPU cores could be fully utilized. One of the main challenges was ensuring accuracy when merging results and avoiding race conditions. Overall, the exercise showed that while parallelism can improve performance for heavy workloads, it can be unnecessary or even inefficient for smaller ones. This typical scenario demonstrates that both approaches are effective but differ in their appropriate use cases.

**Gerlie Campion:** 

I think sequential and parallel differs to each other when it comes to its performance. It was observed in the comparing the time of execution, the two approach differs on how it handles the multiple datasets. Parallel outperform the sequential when it comes to large datasets and vice versa. These observations of mine just conclude that they differ to each other when it comes to their application for a certain dataset. 

**John Carl Ramirez**

This project highlights the trade-off between architectural simplicity and computational throughput. While sequential algorithms remain more efficient for smaller datasets due to the absence of threading overhead, parallel execution proves essential for high-volume workloads where multi-core utilization can significantly reduce execution time. The implementation process underscored the complexities of synchronization and resource management, particularly in avoiding race conditions during the merging of sub-tasks. Ultimately, the results demonstrate that selecting the optimal execution model is strictly dependent on the scale of the dataset and the specific hardware constraints involved.

**Kathleen Grace S. Gultiano**

This activity shows that choosing between sequential and parallel processing is entirely situational, depending heavily on data size and hardware capabilities. While sequential algorithms are straightforward to design and highly efficient for small datasets due to their lack of overhead, they struggle with massive workloads. In contrast, parallel execution requires meticulous attention to task synchronization to prevent race conditions, but its ability to leverage multi-core throughput makes it vastly superior for high-volume tasks. Basically, the decision to use parallel processing should strictly depend on whether the dataset is massive enough to offset the added complexity.

**Francis Adrian Esteban:** 

The comparison between sequential and parallel algorithms was quite enlightening. I noticed that the performance gains from parallel execution are most evident with larger datasets, where the workload can be effectively distributed across multiple cores. However, the overhead of managing threads and ensuring data consistency can negate these benefits for smaller datasets. This project reinforced the importance of understanding the problem domain and hardware constraints when choosing an algorithmic approach. It also highlighted the complexities involved in parallel programming, such as synchronization and potential race conditions. Overall, this exercise provided valuable insights into the trade-offs between simplicity and performance in algorithm design.
