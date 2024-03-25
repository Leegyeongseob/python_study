# # 리스트란? 연속적으로 저장되는 형태의 자료형, 크기가 동적으로 변함
# # 자바와 다른점은 여러가지 데이터 타입이 섞여 있을 수 있음. 리스트내에 리스트가 존재할 수 있음.
# number = [1, 2, 3, 4, 5, 6, 7]
# fruits = ['apple', 'orange', 'banana']
# mixed = [True, 'apple', 3.14, 1]
#
# # 변수와 리스트의 차이
#
# new_list = [1, 2, 3]
# new_list.append(4)
# new_list.append(5)
# new_list.insert(1, 1000)  # 1번 인덱스에 값 추가
# print(new_list)
# # 리스트에서 값 제거하기 : pop, remove, clear
# # pop : 인덱스가 없으면 마지막 인덱스의 값을 변환하고 삭제
# print(new_list.pop())  # 맨 마지막의 5를 반환하고 제거,인덱스를 주면 인덱스 반환하고 제거
# # new_list.remove(3) # 해당 값을 제거, 동일한 값이 여러개 존재하는 경우에는 낮은 인덱스의 값 제거
# # print(new_list)
# # new_list.clear() #내용을 전부 제거하지만 리스트는 제거하지 않음
# # print(new_list)
# del new_list[3] # 해당 인덱스의 값 제거
#
# print(new_list)
#
#
# 중복 제거
# my_list = ["A", " B", " C", "D"," B","C","E"]
# new_list =[]
# for e in my_list:
#     if e not in new_list:
#         new_list.append(e)
# print(new_list)
#
# # 리스트  순회하기
# x = ['John', "George", "Paul", "Ringo"]
# for e in x:
#     print(e, end=" ")
# for i in range(len(x)):
#     print(x[i],end=" ")

# 1~45까지의 로또 번호 6개를 자동 생성하기, 중복 제거
# import random
#
# lotto = []
# while True:
#     rand = random.randrange(1, 46)
#     if len(lotto) == 6: break
#     if rand not in lotto:
#         lotto.append(rand)
#     else:
#         continue
# print(lotto)
#
# # 임의의 수를 연속(공백)으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
# oddList = []
# evenList = []
# for e in list(map(int, input("숫자 입력: ").split())):
#     if e % 2 == 0:
#         evenList.append(e)
#     else:
#         oddList.append(e)
# print(oddList)
# print(evenList)

# 람다를 이용한 풀이
num = list(map(int, input("정수 입력 : ").split()))
str1 = "string"
even = list(filter(lambda x: x % 2 == 0, num))  # 한번만 사용하고 싶을때
odd = list(filter(lambda x: x % 2 == 1, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")
n = list(filter(lambda x:x =="s" or x=="i",str1))
print(n)
n2 = (2,4,5,7,8,9,4,5,"34326","34377")
n2 = list(filter(lambda x:type(x) == str,n2))
print(n2)
