# 파이썬의 변수는 함수 스코프 따름.
# 전역에서 선언된 변수 중 immutable특성을 가진 경우에는 global 키워드 사용해야 함
# 대부분의 경우에서 전역변수를 사용하는 것보다 매개변수로 전달하는 것이 문제(Side Effect)
# 발생 확률을 줄일 수 있음.

knife = 10


def Game(player):
    global knife
    knife -= player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")


def Game2(player, knife):
    knife -= player
    print(f"남아있는 칼은 {knife} 자루 입니다.")


player = int(input("경기에 참여하는 선수가 몇 명 입니까? "))
# Game(player) # side effect가 발생할 확률이 높음.
Game2(player,knife)
