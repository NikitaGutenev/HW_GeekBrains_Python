# #1

# n=float(input())
# num=str(n)
# summ = 0
# for i in num:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)


#2

# n = int(input())
# summ=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         summ*=j
#     print(summ,end=' ')
#     summ=1



#3

# n = int(input())
# summ=0
# for i in range(1,n+1):
#     summ+=(1+1/i)**i
# print(summ)


#4

# n = int(input())
# arr: int = []
# for i in range(-n,n+1):
#     arr.append(i)
# if n<2:
#     print('Число слишком короткое!')
#     exit()
# else:
#     print(*arr)
#     summ = 0
#     with open('file(hw_2).txt','r') as data:
#         for i in data:
#             j = int(i)
#             summ+=arr[j]
#     print(summ)








# #5
# import random as rn
# list1 = list(input().split(' '))
# rn.shuffle(list1)
# print(*list1)


