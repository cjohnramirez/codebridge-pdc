## Analysis Questions

1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.

    **Task Parallelism** involves executing different jobs simultaneously. We demonstrated this in our `compute_deductions` function by running the SSS, Tax, and PhilHealth calculations at the same time for a single person. We divided the work by **function type**. This division works because the formulas don't rely on each other, allowing us to generate the result for one employee much faster.

    **Data Parallelism** involves executing the same job on many items simultaneously. In our lab, this applies to how we handle the list of employees. Instead of looping through them one by one, we can process multiple employees at once. We divide the work by the **amount of data**. This is justified because one employee's salary doesn't affect another's, allowing us to finish the whole group's payroll more efficiently.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor. 

    **How it Manages Execution**
    The `concurrent.futures` module provides a high-level interface for asynchronously executing callables. In our lab, the `ThreadPoolExecutor` managed a pool of worker threads, automatically assigning tasks to available threads so we didn't have to manually create and join them.

    * **`submit()`:** We used this method to schedule a specific function (like `sss_deduction`) to run immediately on a separate thread. It returns a `Future` object instantly, allowing the main program to keep running while the calculation happens in the background.

    * **`map()`:** Although we used `submit` in the lab, `map()` is designed to apply a function to a list of items (like a list of employees) in parallel. It handles the loop for us and returns the results in the same order as the inputs.

    * **`Future` Objects:** These act as "claim stubs" for results that aren't ready yet. When we call `.result()` on a `Future`, the program pauses and waits until that specific thread finishes its task and delivers the value.

    We used the `with` statement to create a context manager for the executor, ensuring that our thread pool was properly initialized and managed without manual cleanup. Its most critical function is to automatically trigger a shutdown when the code block exits, forcing the main program to wait until all threads have finished their tasks. This approach keeps our resource management clean and prevents the application from terminating prematurely while background work is still in progress.

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur? 

    The execution managed by ThreadPoolExecutor in this lab activity was constrained by Python's Global Interpreter Lock (GIL), which prevents multiple threads from executing Python bytecodes simultaneously on different CPU cores. Because the deduction tasks were CPU-bound mathematical operations rather than I/O waiting periods, **true parallelism did not occur**. Instead, the threads merely achieved concurrency through rapid context switching on a single core, meaning the tasks were managed at the same time but never actually ran at the exact same instant, offering no performance gain over sequential execution for this specific workload.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior. 

    ProcessPoolExecutor enables true parallelism because each worker runs in a separate process with its own independent memory space and Python interpreter. Unlike threads, processes do not share the same Global Interpreter Lock (GIL), meaning each process has its own GIL instance and can execute Python bytecode simultaneously on different CPU cores. This avoids the bottleneck where only one thread runs at a time in CPU-bound tasks. Memory separation also reduces contention and race conditions since processes do not directly share variables. As a result, CPU-heavy computations like payroll deductions can run in real parallel across multiple cores.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
    
    If the system grows from 5 to 10,000 employees, a thread-based approach becomes inefficient because thousands of threads cause heavy context switching, memory overhead, and GIL contention. Even with many threads, only one executes Python code at a time, limiting speed improvements. In contrast, a process-based approach distributes employees across a fixed number of worker processes equal to the CPU cores, enabling true parallel execution. This keeps resource usage controlled while maximizing CPU utilization. Therefore, ProcessPoolExecutor scales significantly better for large payroll workloads.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.

    In a real-world payroll system, each employee’s salary must be processed by computing independent deductions such as SSS, PhilHealth, Pag-IBIG, and withholding tax. Task parallelism can be applied within a single employee by running these deduction functions concurrently using a ThreadPoolExecutor since they are small, independent tasks that share the same data. Data parallelism is applied across many employees by processing multiple employees simultaneously using a ProcessPoolExecutor, which fully utilizes multiple CPU cores. This hybrid approach combines fast per-employee concurrency with scalable multi-core processing. It ensures the payroll system remains efficient even when handling thousands of employees.