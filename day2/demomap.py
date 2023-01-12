# def add(num):
#     return num+10
# price = [2,4,6,7,8,9]
# new_price=[]
# for p in price:
#     new_price.append(add(p))
# print(new_price)
#
# new_price=map(add,price)
# print(list(new_price))
def task(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
        if(c==2):
            return a
l=[1,2,4,5,7,8,12,11]
r=list(map(task,l))
print(r)


