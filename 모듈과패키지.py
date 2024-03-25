# 모듈 : python 코드를 포함하는 파일(.py)
# 모듈에는 함수, 클래스, 변수 등을 포함 할 수 있으며
# 이러한 요소들은 다른 python 파일에서 import해서 사용 할 수 있음.
# 패키지 : 모듈의 집합, 즉 여러개의 모듈을 포함하는 디렉토리를 의미

# 나만의 모듈만들기

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password


# 진입지점이 바로 이 파일이면 실행!!
# 다른 파일이면 실행 X
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
