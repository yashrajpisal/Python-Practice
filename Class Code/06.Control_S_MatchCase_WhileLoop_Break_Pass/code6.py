
day = input("Enteer day : ")

match day:
    case "Mon":
        print("Start of the week")
    case "Fri":
        print("Weekend is coming")
    case "Sat":
        print("Weekend Started")
    case "Sun" :
        print("Relax, it's sunday")
    case _:
        print("Weekday")

