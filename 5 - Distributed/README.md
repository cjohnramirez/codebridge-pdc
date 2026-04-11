Reflection Questions (Answers)
1. How did you distribute orders among worker processes?
  
    We distributed the orders among worker processes using MPI message passing. The master process used a round-robin method to send each order to different workers.

2. What happens if there are more orders than workers?
   
   If there are more orders than workers, some workers receive and process multiple orders. This helps balance the workload across all processes.

3. How did processing delays affect the order completion?
    
    Processing delays affected the order completion because each worker had a random delay. This caused the orders to finish at different and unpredictable times.

4. How did you implement shared memory, and where was it initialized?

    We did not use actual shared memory in this program. Instead, we used MPI message passing where workers send their results back to the master process.

5. What issues occurred when multiple workers wrote to shared memory simultaneously?

    There were no direct shared memory conflicts because MPI handles communication through messages. If shared memory were used, multiple workers writing at the same time could cause data issues.

6. How did you ensure consistent results when using multiple processes?

    We ensured consistent results by collecting all outputs in the master process using comm.recv(). We also used unique order IDs and message tags to organize communication properly