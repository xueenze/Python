print(list(range(1,11)))

print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os

print([d for d in os.listdir('.')])

print(os.listdir('.'))

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k,v in d.items()])
