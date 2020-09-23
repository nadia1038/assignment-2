a = input(int())
b = input(int())



#case 01 : 3,4

if a>b:
    print("the number is: " + a)
elif b>a:
    print("the number is: " + b)
elif a==b:
    print("they are equal")
else:
    print("i don't know")
    
#case 02 : 3,3

if a>b:
    print("the number is: " + a)
elif b>a:
    print("the number is: " + b)
elif a==b:
    print("they are equal")
else:
    print("i don't know")

#case 03 : 9,7

if a>b:
    print("the number is: " + a)
elif b>a:
    print("the number is: " + b)
elif a==b:
    print("they are equal")
else:
    print("i don't know")
   
   
#case 04 : 2,9

if a>b or a!=b:
    if a>b:
        print("a is greater")
    elif a!=b:
        print("ok")
elif a==b:
    print("they are equal")
elif b>a:
    print("b is greater")
else:
    print("i don't know")

#case 05 : 5,9

if a>b and a!=b:
    if a>b:
        print("a is greater")
    elif a!=b:
        print("ok")
elif b>a or b==a:
    if b>a:
        print("this is the answer")
    elif b==a:
        print("they are equal")
else:
    print("i don't know")
    
    
