def monisha(arg):
    print("ID of argument",id(arg))
    arg=arg
    print("New object", id(arg))
var = 10
print(id(var))
monisha(var)
print(var)
