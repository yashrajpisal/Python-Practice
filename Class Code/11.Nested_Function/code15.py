

def outerFunc():
    print("In outerr function")

    def innerFunc1():
        print("IN inner func1")
    def innerFunc2():
        print("In inner func2")

    print(innerFunc1)
    print(innerFunc2)

print(outerFunc)
outerFunc()
