


def outerFunc():
    print("In OuterFunc")
    
    def innerFunc():
        print("In InnerFunc")
    innerFunc()

outerFunc()

