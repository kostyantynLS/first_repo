def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer()  # 5
