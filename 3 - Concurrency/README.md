## Analysis Questions
### Provide concise but well-structured explanations. 

1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor. 

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur? 

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior. 

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
 
6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
