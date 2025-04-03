# AF to take input and print a table of the input till 100
n=int(input("give an input:")) #input of a number
def calculate_table(): #func defined
    x=0
    while x<=100:
      print(f"{n}*{x}=",n*x)
      x+=1

calculate_table() #call the func
