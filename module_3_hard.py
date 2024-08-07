data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    total_amount = 0
    for i in args:
        if isinstance(i, str):
            total_amount += len(i)
        elif isinstance(i, (int, float)):
            total_amount += i
        elif isinstance(i, (list, tuple, set)):
            total_amount += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            total_amount += calculate_structure_sum(*i.items())
        elif i is None:
            pass
    return total_amount

result = calculate_structure_sum(data_structure)
print(result)
