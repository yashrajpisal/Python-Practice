def fun():
    x = 10
    y = 20
    z = 30
    print("Fun x:",x)
    print("Fun y:",y)
    print("Fun z:",z)
    def gun():
        x = 40
        y = 50
        z = 60
        print("Gun x:",x)
        print("Gun y:",y)
        print("Gun z:",z)
    return gun
retGun = fun()
retGun()
print(retGun.__closure__)
