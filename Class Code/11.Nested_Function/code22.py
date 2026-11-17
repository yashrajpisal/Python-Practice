

def outerFunc():
    print("In outer func")

    def innerFunc1():
        print("In inner func1")
    def innerFunc2():
        print("In inner func2")

    return innerFunc1 , innerFunc2
retVal = outerFunc()
print(type(retVal))
