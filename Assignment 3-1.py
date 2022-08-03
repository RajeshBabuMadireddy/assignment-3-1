sumofnum=[]
n=int(input('enter the length of list'))
for i in range(0,n):
    element=int(input())
    sumofnum.append(element)
def sumoflist(list,size):
        if(size==0):
            return 0
        else:
            return list[size-1]+sumoflist(list,size-1)
sum=sumoflist(sumofnum,len(sumofnum))
print('sum of elements :',sum)