print("The number of guesses are 9")
var1=69
i=9
while i>0:
    print ("Please enter your number ")
    var2=int(input())
    i=i-1
    print(" Guesses remaning:",i)
    if var2>var1:
        print(" smaller")
    if var2<var1:
        print("greater")
    if var2==var1:
        print("Congratulations")
        break 
while i==0:
    print("Sorry better luck next time")
    break 