

dict1={'empno':'940','empname':'siva','empage':'21','empcity':'tuty','empsalary':'40000'}
print("Dictionary is:",dict1)
print("employee name:",dict1['empname'])
print("employee city:",dict1['empcity'])
print("employee salary:",dict1['empsalary'])
print("All Keys in Dictionary")
for x in dict1:
    print(x)
print("All Values in Dictionary")
for x in dict1:
    print(dict1[x])
dict1["phno"]=9087654321
dict1["emprole"]="Assistant Manager"
print("Updated dictionary:",dict1)
dict1['empname']='sundari'
print("Updated dictionary:",dict1)
dict1.pop("empage")
print("Updated Dictionary:",dict1)
print("Length of the dictionary:",len(dict1))
dict2=dict1.copy()
print("New dictionary:",dict2)
dict1.clear()
print("Updated Dictionary:",dict1)
