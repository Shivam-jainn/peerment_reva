

def main():
    a = getcs()
    change = cschange(a)
    print(change)


def getcs():
    a = input()
    return a

def cschange(a):
    listhai = []
    f = a.split(";")
    for i in f:
        b = i.split("=")
        c = tuple(b)
        # print(c)
        listhai.append(c)
    return listhai
        

if __name__ == "__main__":
    main()