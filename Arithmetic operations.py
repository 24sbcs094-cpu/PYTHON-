def add (a,b):
    return a+b
def sub (c,d):
    return c-d
def mul (e,f):
    return e*f
def div (g,h):
    return g%h
print("==================")
print("1.To perform Addition")
print("2.To perform Subtraction")
print("3.To perform Multiplication")
print("4 To perfrom Division")
print("5 Exit")
print("=================")

while(1):
    choice=int(input("Enter your choice"))
    if choice==1:
        a=int(input("Enter a value for A"))
        b=int(input("Enter a value for B"))
        print(add(a,b))
    elif choice==2:
        c=int(input("Enter a value for C"))
        d=int(input("Enter a value for D"))
        print(sub(c,d))
    elif choice==3:
        e=int(input("Enter a value for E"))
        f=int(input("Enter a value for F"))
        print(mul(e,f))
    elif choice==4:
        g=int(input("Enter a value for G"))
        h=int(input("Enter a value for H"))
        print(div(g,h))
    elif choice==5:
        print("Exited")
        break
    else:
        print("Wrong Choice")     
        
    

        
        
        
        
        
        
