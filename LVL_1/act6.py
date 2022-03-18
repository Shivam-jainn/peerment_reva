
def main():
    cs = getcs()
    dict_cs = cs_to_dict(cs)

def cs_to_dict(cs):
    dicthai = {}
    cssplit = cs.split(";")
    for i in cssplit:
        splitpart = i.split("=")
        dicthai[splitpart[0]] = splitpart[1]
    print(dicthai)
    

def getcs():
    cs = input()
    return cs

if __name__ == "__main__":
    main()