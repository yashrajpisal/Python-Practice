

def outerFunc():
    print("In outer func")
    x = 20
    def innerFunc():
        print("In inner func")

    return innerFunc
retVal = outerFunc()
(retVal())


