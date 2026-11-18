

x = 10
def fun():
    x = 20
    print("Fun x : ",x)
    def gun():
        x = x+1

        print("gun x :",x)
    return gun

print(x)                       #10

retVal = fun()                 #fun x : 20
retVal()                       #error
