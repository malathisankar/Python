def sum():
    a=5
    b=10
    def add():
        nonlocal a
        nonlocal b
        print(a)
        print(b)
        return a+b
    print(add())
sum()
