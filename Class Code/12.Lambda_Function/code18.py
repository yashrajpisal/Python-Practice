

def fun(a):
    print("In fun before :",a)
    a = 30
    print("In fun after : ",a)

x = 10
print("global before :",x)
fun(x)
print("global after :",x)
