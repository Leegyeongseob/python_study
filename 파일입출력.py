# scoreFile = open("./score.txt", "w", encoding="utf-8")
# print("수학 : 55", file=scoreFile)
# print("영어 : 60", file=scoreFile)
# scoreFile.write("과학 : 90\n")  # 프린트는 줄바꿈이 있지만 쓸때는 줄 바꿈이 없다.
# scoreFile.write("국어 : 100\n")
# scoreFile.close()
# # 파일 읽기
# scoreFile = open("score.txt", "r", encoding='utf-8')
# # read() 함수 : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# print(scoreFile.read()) # 너무 큰 파일은 버퍼에 무리가 가서 read는 고려해 볼 필요가 있다.
# scoreFile.close()
#
# # readLine()함수 : 한 라인씩 읽어 문자열로 반환, 파일의 끝에 도달하면 None값이 반환
# while True:
#     line = scoreFile.readLine() # 한 라인씩 읽음. 읽을게 없으면 None
#     if not line: break
#     print(line, end="")
# scoreFile.close()

# readlines() : 해당 파일의 모든 라인을 순서대로 읽어들여 리스트로 반환
# lines = scoreFile.readlines() # 파일의 라인을 리스트로 반환
# for line in lines: # 시퀀스가 온다.
#     print(line, end="")
#     scoreFile.close()

# with 구문을 사용하면 구문이 종료 될 때 자동으로 파일을 닫음.
# with open("score.txt", "r", encoding="utf-8") as scoreFlie:
#     lines = scoreFlie.readlines()
#     for line in lines:
#         print(line, end="")


