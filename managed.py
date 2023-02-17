from prefect import task, flow
import random
import time

@task(log_prints=True)
def my_task(num: int) -> int:
    print(f"the task number is {num}")
    output_int = random.randint(1,5)
    time.sleep(output_int)
    return output_int

@task(log_prints=True)
def my_sleepy_task(num_to_sleep: int) -> None:
    print("I'm sleepy")
    time.sleep(num_to_sleep)

@flow(log_prints=True)
def my_flow(num_tasks: int) -> None:
    print("flow starting")
    for i in range(num_tasks):
        second_num = my_task.submit(num=i)
        for j in range(second_num.result()):
            my_sleepy_task.submit(second_num.result())


if __name__ == "__main__":
    num_tasks = random.randint(50,60)
    my_flow(num_tasks=num_tasks)
    