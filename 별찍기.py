# 문제 1번
#
# n = int(input("정수를 입력 하세요 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:3}", end='')    #이쁘게 찍기 위해서 오른쪽 정렬 한다. 왼쪽 정렬은 <
#     if i % n == 0: print()
#
# # 문제 2번
#
# n2 = int(input("n값을 입력해주세요: "))
# for i in range(n2,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
#
# # 문제 3번
#
# n3 = int(input("n값을 입력해주세요: "))
# for i in range(n3):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n3-i,0, -1):
#         print("*",end="")
#     print()

# # for문에서 continue 사용
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i, end=" ")
#
# # for문을 반대로 반복하기
# for i in range(10,-1,-1): #범위가 10에서부터 1씩 감소시키면서 0이 될때까지 반복
#     print(f"index : {i}")

#for문으로 알파벳 출력하기
#chr(유니코드값을 입력 받아 문자 출력)
#ord(문자의 유니 코드 값을 반환)
# for i in range(ord("A"), ord("Z")+1):
#     print(chr(i),end="")
# print()
#
# for i in range(65,91): #A 65 , Z:90
#     print(chr(i),end="")
# print()