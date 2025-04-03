n=int(input("give an input:"))
def calculate_table():
    x=0
    while x<=100:
      print(f"{n}*{x}=",n*x)
      x+=1

calculate_table()