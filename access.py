import time

sizes = [10, 100, 1000, 10000, 100000, 500000]
target_factor = 0.9

print(f"{'Size':>8} | {'List':>10} | {'Set':>10} | {'Tuple':>10} | {'Dict':>10}")
print("-" * 60)

for size in sizes:
    target = int(size * target_factor)

    test_list = list(range(size))
    test_set = set(range(size))
    test_tuple = tuple(range(size))
    test_dict = {i: None for i in range(size)}

    start = time.perf_counter()
    _ = target in test_list
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = target in test_set
    set_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = target in test_tuple
    tuple_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = target in test_dict
    dict_time = time.perf_counter() - start

    print(f"{size:8} | {list_time:10.8f} | {set_time:10.8f} | {tuple_time:10.8f} | {dict_time:10.8f}")
