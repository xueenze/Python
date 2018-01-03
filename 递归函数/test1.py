def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(12))

# 解决递归调用栈溢出的方法是通过尾递归优化
def fact(n):
    return fact_filter(n, 1)

def fact_filter(num, product):
    if num == 1:
        return product
    return fact_filter(num - 1, num * product)
