def strlen(str):
    Counter=0
    while str[Counter:]:
        Counter+=1
        return Counter
def strrev(str):
    rstr=" "
    l=strlen(str)
    while l>0:
        rstr=rstr+str[l-1]
        l=l-1
        return rstr
def strcat(str1,str2):
    return str1+str2
def strcmp(str1,str2):
    if(st1==st2):
        print(str1,"and",str2,"are same")
    elif(str1>str2):
        print(str1,"are",str2,"is in after the dictionary")
    else:
        print(str1,"are",str2,"is in before the dictionary")
print("Funtions")
print("=============")
print("1.String length")
print("2.String Reverse")
print("3.String concanetation")
print("4.String Compare")
print("5.Exit")
print("=============")
while(1):
    n=int(input("Enter Your Choice"))
    if(n==1):
          str=input("Enter a word")
          print(strlen(str))
    elif(n==2):
          str=input("Enter a word to reverse")
          print(strrev(str))
    elif(n==3):
          str1=("Enter a first word")
          str2=("Enter a second word")
          print(strcat(str1,str2))
    elif(n==4):
          str1=("Enter a frst word")
          str2=("Enter a second word")
          print(str1cmp(str1,str2))
    elif(n==5):
          print("Exited")
          break
    else:
          print("Your are out of box sorry")
                
          
      
    

    
