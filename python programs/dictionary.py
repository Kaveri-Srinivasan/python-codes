import re
dict1={"testke98y1":"123456",
       "12testkey2":"testval"
}
dict2={}
for key,value in dict1.items():
    x=re.sub('[0-9]',"_",key)
    if x.isdigit():
       x="_".join(x)
    dict2[x]=value
print(dict2)

