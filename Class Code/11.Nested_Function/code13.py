


def outerFunc():
    print("In outerr function")

    def innerFunc():
        print("In inner function")
        
    print(innerFunc)
print(outerFunc)

