

start = int(input("Enter Start num: "))
end = int(input("Enter End num : "))

while start <= end:
    if start % 3 == 0 and start % 5 == 0:
        print(start)

    start+=1
