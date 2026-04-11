from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ---------------- SAFETY CHECK ----------------
if size < 2:
    if rank == 0:
        print("ERROR: Run with at least 2 processes using mpiexec -n 4")
    exit()
