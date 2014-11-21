import itertools

lst = [1, 2, 3]
combs = []

for i in xrange(1, len(lst)+1):
    combs.append(i)
    print [list(x) for x in itertools.combinations(lst, i)]
print combs