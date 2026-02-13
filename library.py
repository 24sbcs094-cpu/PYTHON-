d=int(input("enter a days:"))
fine=0
if(d<=5):
    fine=d*5
    print("Fine:",fine)
elif(d>5 and d<10):
    i=d-5
    fine=(i*1)+(5*5)
    print("Fine:",fine)
elif(d>10 and d<30):
    i=d-10
    fine=(i*1)+(5*5)+(5*2)
    print("Fine:",fine)
else:
    i=d-10
    fine=(i*1)+(5*5)+(5*2)
    print("Your Member ship is cancelled")
    print("Fine:",fine)
    
