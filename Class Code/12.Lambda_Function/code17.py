

def fun(x):
    print("In fun before :",x)
    x = 30
    print("In fun after : ",x)

x = 10
print("global before :",x)
fun(x)
print("global after :",x)
