# n=int(input("enter the num"))
# if n%2==0:
#     print("even no = ",n)
# else:
#     print("odd no = ",n)


# a=int(input("enter the number user:"))
# if a<0:
#     print(-a)
# else :
#     print(-a)

# for i in range(1,11):
#     print(i)

# i=11
# while i>1:
#     i=i-1
#     print(i)

# n=[1,1,2,3,2,4,3,5,5]
# a=[]
# for i in n:
#     if i not in a:
#         a.append(i)
# print(a)

# n=[10,2,3,6,8,9,3,4,5,]
# a=0
# b=0
# for i in n:
#     if i > a:
#         b=a
#         a=i
#     elif i > b:
#         b=i
# print(b)


# n=[1,2,3,4,]
# a=0
# b=0
# for i in n:
#     if i > a:
#         b=a
#         a=i
#     elif i > b:
#         b=i
# print("secand positive no.  :" ,b)

def add():
    a=[]
    sum=0
    avg=0
    b=3
    i=0
    while i<b:
        n=int(input("enter the num"))
        a.append(b)
        sum=sum+n
        avg=sum/b
        i+=1
    print("sum of three num= ",sum)
    print("avg of three num= ",avg)
add()
        

  
