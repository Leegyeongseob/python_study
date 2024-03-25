# 문제 1.
# def Chackevenodd(n):
#     if n % 2 == 0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
#
# n = int(input("정수 입력 : "))
# Chackevenodd(n)

# 문제 2.
# def Avarage(listNum):
#     return sum(listNum) / len(listNum)
#
#
# listNum = list(map(int, input("숫자들 입력 :").split()))
# print(Avarage(listNum))

def Primefunc(n):
    sum = 0
    for i in range(2,n):
       for j in range(1,i):
           if j % i == 0:
               continue
           else:
               sum+=i
    return sum


num = int(input("숫자 입력 : "))
print(Primefunc(num))



