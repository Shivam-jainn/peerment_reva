def add(a,b):
    c = a+b
    return c

def input_nu():
  a=int(input ("enter number a :"))
  b=int(input ("enter number b:"))
  return a,b

def main():  
  a,b  = input_nu()
  sumhai = add(a,b)
  print (sumhai)

if __name__ == "__main__":
  main()