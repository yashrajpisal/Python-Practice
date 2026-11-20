

#x = 20
def fun():
    x = 10
    print("fun x:",x)
    def gun():
        #global x
        #nonlocal x
        x=x+1
        print("gun x:",x)

    return gun
retRef = fun()
retRef()
