L = []
class menu:
    def add(item,name,price) :
         item.price = price
         item.name = name
         
    def add(item,name,price):
        L.append((name,price))    
    def show(self):
        print(str(L))

m = menu()
def main():
    m.add("idly",10)
    m.add("vada",20)
    m.show()

if __name__=="__main__":
    main()

        
    