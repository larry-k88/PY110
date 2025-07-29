# A developer is trying to remove duplicates from a list. They use a set
# for deduplication, but the order of elements is lost. How can we
# preserve the order?

''' Set removes duplicates but is an unordered collection
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data)
'''

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

seen = set()
unique_data = []
for num in data:
    if num not in seen:
        unique_data.append(num)
        seen.add(num)

print(unique_data == [4, 2, 1, 3])