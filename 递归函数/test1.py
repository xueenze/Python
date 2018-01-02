def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(12))

# 解决递归调用栈溢出的方法是通过尾递归优化