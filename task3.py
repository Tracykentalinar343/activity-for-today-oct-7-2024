names = ["tracy","kent","MC","KENLY"]
num = input("clear ot not:")
if num  == "clear":
    enter = input("who:")
    if enter == "tracy":
        names.pop(0)
        print(names)
    elif enter == "kent":
        names.pop(1)
        print(names)
    elif enter == "Mc":
        names.pop(2)
        print(names)
    elif enter == "KENLY":
        names.pop(3)
        print(names)
    else:
        print("error")
else:
    print("names")