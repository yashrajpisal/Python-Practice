

x = 10
def fun():
    global x
    x=20
    print("in fun:",x)
print(x)
fun()
print(x)
