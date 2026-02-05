from functools import lru_cache
from time import perf_counter


def timer(f):
    def timer_wrapper(*args, **kwargs):
        t0 = perf_counter()
        n = f(*args, **kwargs)
        t1 = perf_counter()
        print(f"finished in {t1-t0}s: f{*args,kwargs} -> {n}")
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
