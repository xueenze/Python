f = open('test.txt', 'r')
print(f.read())

for line in f.readlines():
    print(line.strip())

with open('test.txt', 'r') as f:
    print(f.read())

f = open('test.txt', 'w')
f.write('Hello World')

with open('test.txt', 'a') as f:
    f.write('Hell Yes')