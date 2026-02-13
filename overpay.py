overpay=0
for i in range(1,11):
    print("Enter the hours of employee:",i)
    hours=int(input())
    if(hours>40):
        extra=hours-40
        overpay=extra*12
        print("over pay for your extra wrok is:",overpay)
    else:
        print("No extra pay ")
        
