def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

def custom_min(lst):
    return min(lst)

def custom_max(lst):
    return max(lst)

def custom_len(lst):
    return len(lst)

def custom_sum(lst):
    return sum(lst)

def custom_sorted(lst):
    return sorted(lst)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))