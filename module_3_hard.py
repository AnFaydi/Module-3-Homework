def calculate_structure_sum(args):
    sum = int()
    for element in args:
        if isinstance(element,(list, tuple, set)):
            sum += calculate_structure_sum(element)
        if isinstance(element, dict):
            element = list(element.items())
            sum += calculate_structure_sum(element)
        if isinstance(element, str):
            sum += len(element)
        if isinstance(element, int):
            sum += element
    return sum
data_structure1 = [[1, 2, 3], 1,'s', {'a':4}]
data_structure2 = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result1 = calculate_structure_sum(data_structure1)
print(result1)
result2 = calculate_structure_sum(data_structure2)
print(result2)