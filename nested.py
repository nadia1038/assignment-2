#nested if else

#example 01
a = 10
b = 20
c = 30
(x,y) = (40,50)
subject1 = "englsh"
subject2 = "Math"

if a>=b or b>=c or subject1=="math":
    if a>=b:
        print("a is greater")
    elif b>=c:
        print("b is greater")
    elif subject1== "math":
        print("math")
elif y>x>c>b>a or x+y<200 and subject1=="english":
    if a+b<10:
        print(" equal")
    elif a+x>y:
         print("greater")
    elif b+y==70:
        c=b+x
        print(c) #this is the answer(60)
elif a>b>c>x>y or subject2=="english":
    if b>a:
        print("this is not the answer")
    elif subject1== "math":
        print("not answer")
else:
    ("i dont know")
    

#example 02

a=5
b=10
c=15
d=20
e=25
if e>d>c>b>a and b/a==2 and a+b>10:
    if a==b+c:
        print("No 1")
    elif a+b+c<=d:
        print("no 2")
    elif d+e>=45:
        if d+e> 45:
            print("no 3")
        elif e<a:
            print("no 4")
        elif d+e==45 or a>b:
            if e<=b:
                print("no 5")
            elif e+d>=a+b:
                print((a+b)/c) #this is the answer(1)
elif a>b>c>d>e or b+c>a+b:
    if a>b>c:
        print("no 6")
    elif e<c+d:
        print("no 7")
    
else:
    ("i dont know")
