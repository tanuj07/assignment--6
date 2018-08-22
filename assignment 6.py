#Question 1
def area(num):
    return(num*num)
num=int(input("enter a side"))
print(area(num))

#Question 2
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print(num)
for j in range(1,1000):
    perfect(j)

#Question 3
def table(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)
n=int(input("enter number"))
table(n)

#Question 4
def cal(num,pow):
    if pow!=0:
        return(num*cal(num,pow-1))
    else:
        return 1
num=int(input("enter number"))
pow=int(input("enter power"))
print(cal(num,pow))
