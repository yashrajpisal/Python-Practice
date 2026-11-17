


def outerFunc():
    print("In OuterFunc")
    def innerFunc():
        print("In InnerFunc")

outerFunc()
innerFunc()
