## Analysis Questions
### Provide concise but well-structured explanations. 

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

    The execution managed by ThreadPoolExecutor in this lab was constrained by Python's Global Interpreter Lock (GIL), which prevents multiple threads from executing Python bytecodes simultaneously on different CPU cores. Because the deduction tasks were CPU-bound mathematical operations rather than I/O waiting periods, **true parallelism did not occur**. Instead, the threads merely achieved concurrency through rapid context switching on a single core, meaning the tasks were managed at the same time but never actually ran at the exact same instant, offering no performance gain over sequential execution for this specific workload.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior. 

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
 
6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
