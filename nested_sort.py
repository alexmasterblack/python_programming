def sorted_two(data, key = lambda x: -x):
    sort_data = []
    for i in data:
        sort_data.append(sorted(i, key = key))
    return sorted(sort_data, key = lambda i: i[-1])

data = [[6, 5, 4], [3, 2], [1]]

key = lambda x: x
print(sorted_two(data, key = key))