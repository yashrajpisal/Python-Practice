


def outerFunc():
    print("in oute function")

    x = 10
    def innerFunc():
        print("In inner func")

    innerFunc()
    return x
outerFunc()
