

#Count Digits

def digitCount(x):
    '''
    a = str(x)
    count = len(a)
    print(count)
    '''
    count = 0
    while x > 0:
        x//=10          #x = x//10
        count+=1
    print(count)

x = 123
#digitCount(x)

# Separate Digits
def sepDigit(x):
    num = x
    rem = 0
    while num>0:
        rem = num%10
        print(rem)
        num//=10
sepDigit(x)



