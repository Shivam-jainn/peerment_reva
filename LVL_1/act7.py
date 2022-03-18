L = []
class menu:
    def __init__(self,item,price) :
        self.price = price
        self.item = item
    def add(self,item,price):
        L.append([self.item,self.price])
    def show(L):
        print(L)


def main():
    m = menu()
    m.add("idly",10)
    m.add("vada",20)
    m.show()

if __name__ == "__main__":
    main()

        
    