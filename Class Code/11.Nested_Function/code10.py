


def outerFunc():
    print("In outer Function")

    def innerFunc1():
        print("In Inner Function1")
    def innerFunc2():
        print("In inner Function2")
    innerFunc1()
    innerFunc2()
    print("End code")

outerFunc()
