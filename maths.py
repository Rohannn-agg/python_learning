# def convert(n):
#     var1=str(n)
#     a=0
#     multiply=1
#     for i in range(0,len(var1)):
#         bit=int(var1[len(var1)-i-1])
#         var2=bit*multiply
#         a=a+var2
#         multiply=multiply*2
#     return a
# inpnum=int(input("Enter your binary code"))
# # print(convert(inpnum))
# # print("-5 7")
# import math 
# var1=math.log(1024,2)
# print(var1)
from math import pow 
c=0
for i in range (1,15):
    for j in range(1,15):
        a=pow(i,3)
        b=pow(j,3)
        if (a+b==1729):
            if (c<2):
                print ("The answer is",i,j)
                c=c+1
            else:
                break 
            
        