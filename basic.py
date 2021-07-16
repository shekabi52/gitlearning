st="bharath msd poda"
st=st.title()
print(st)
st=st.center(20,"*")
print(st)
str1="-"
print(str1.join(st))
str=st.lstrip("*")
print(str)
import re

input = '100klh564abc365bg'
num=re.findall("\d+",input)
num=list(map(int,num))
print(max(num))


for i in range(0,6):
    print("*"*i)