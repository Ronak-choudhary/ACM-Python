#Ques 1
m=int(input("Enter 1st number :"))
n=int(input("Enter 2nd number :"))
sum=0
for i in range(m,n+1):
    sum=sum+i
print("Sum of all numbers between",m,"and",n,"is:",sum)

#Ques 2
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
if a%b==0:
    print(a,"is properly divisible by",b)
elif b%a==0:
    print(b,"is properly divisible by",a)
else:
    print("They are not properly divisible")

#Ques 3
d=int(input("Enter the diameter of the circle :"))
print("Area of circle is :",3.14*(d/2)**2)
print("Perimeter of the circle :",2*3.14*d/2)

#Ques 4
f=int(input("Enter your number :"))
fact=1
for i in range(f,1,-1):
    fact=fact*i
print("Factorial of the given number is :",fact)

#Ques 5
for i in range(1,7):
    for j in range(1,i):
        print(j,end="")
    print()
    
