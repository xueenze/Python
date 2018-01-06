def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

print(next(_odd_iter()))

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = odd_iter()

    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

print(next(primes()))
