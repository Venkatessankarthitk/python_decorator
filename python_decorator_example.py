
from functools import wraps
def timed(fn):
    from time import perf_counter
   
   
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end -start
       
        args_ = [str(a) for a in args]
        kwargs_ = ["{0}={1}".format(k ,v ) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = '.'.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
        args_str, elapsed))
        return result
    return inner

def logged(fn):
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
       
        result = fn(*args, **kwargs)
       
        print('{0} called  {1}'.format(run_dt , fn.__name__))
        return result
    return inner

# def calc_recursive_fib(n):
#     if n <=2:
#         return 1
#     else:
#         return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)
       
       

# @logged
# @timed
# def fib_recuresive(n):
#     return calc_recursive_fib(n)

# print(fib_recuresive(39))

# @timed
# def fib_loop(n):
#     fib_1 = 1
#     fib_2 = 1
#     for i in range(3, n+1):
#         fib_1, fib_2 = fib_2, fib_1 + fib_2
#     return fib_2
   
# print(fib_loop(39))

# import functools

# @timed
# def fib_reduce(n):
#     initial = (1,0)
#     dummy = range(n)
#     fab_n = functools.reduce(lambda prev, n:(prev[0]+prev[1], prev[0]), dummy, initial)
#     return fab_n[0]
   
# fib_reduce(39)

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce
   
    return reduce(mul, range(1, n+1))
   
print(fact(3))
