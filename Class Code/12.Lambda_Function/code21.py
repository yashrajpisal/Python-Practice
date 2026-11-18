

def fun(listObj):
    print("In fun : ",listObj)
    listObj[2] = 70
    print("In fun after update: ",listObj)

listObj = [10,20,30,40]
print("In main : ",listObj)
fun(listObj)
print("In main after fun call: ",listObj)
