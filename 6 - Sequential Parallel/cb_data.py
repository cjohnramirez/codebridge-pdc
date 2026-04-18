import random

def CB_generate_data(CB_size):
    return [random.randint(1, 1_000_000) for _ in range(CB_size)]