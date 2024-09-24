from itertools import batched

def all_variants(text):
    count = 1
    while count <= len(text):
        for count_2 in range(count, len(text) + 1):
            yield text[count_2 - count:count_2]
        count +=1

a = all_variants('abc')
for i in a:
    print(i)