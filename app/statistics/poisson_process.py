import math
from matplotlib import pyplot as plt
from numpy import random


def poisson_process(rate, t1):
    """
    Args:
        rate: events/time unit
        t1: number
    Returns:
        times: list of 'times' when event occur
    """

    times = []
    time = 0
    while True:
        rnd = random.rand()
        t = (1 / rate) * math.log(1 - rnd, math.e)
        time -= t
        if time > t1:
            break
        times.append(time)

    for i in range(len(times)):
        print(f"{i} : x < {times[i]}")

    plt.step(times, range(len(times)))
    plt.title("Poisson Process")
    plt.xlabel("Time")
    plt.ylabel("Events")
    plt.show()
    return times


if __name__ == "__main__":
    print("Simulation of python process")
    poisson_process(2, 10)
