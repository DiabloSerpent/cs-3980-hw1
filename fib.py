from functools import lru_cache
from time import perf_counter
import matplotlib.pyplot as plt
import pandas as pd

use_graph = False
graph_data = {}


def timer(f):
    def timer_wrapper(*args, **kwargs):
        t0 = perf_counter()
        n = f(*args, **kwargs)
        t1 = perf_counter()
        ts = t1 - t0
        print(f"finished in {ts}s: f{*args,kwargs} -> {n}")
        if use_graph:
            graph_data[args[0]] = ts
        return n

    return timer_wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)

    if use_graph:
        graph_data = sorted(graph_data.items())
        df = pd.DataFrame(
            {
                "x_axis": [x for (x, y) in graph_data],
                "y_axis": [y for (x, y) in graph_data],
            }
        )
        plt.plot("x_axis", "y_axis", data=df, linestyle="-")
        plt.show()
