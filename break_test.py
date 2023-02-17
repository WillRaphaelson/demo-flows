import time
from prefect import flow

GB = 1024 * 1024 * 1024

@flow()
def eat_memory(mem_to_eat=2):
    """
    Eats memeory
    :param mem_to_eat: The amount of memory to eat in gigs
    """
    global GB
    eat = "a" * GB * mem_to_eat
    while True:
        time.sleep(1)