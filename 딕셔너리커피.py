# 딕셔너리를 이용한 커피메뉴 만들기
menuDic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}


# 입력값이 대소문자 구분없도록 추가 구현!

# 중복 key값이 있는 경우 뒤의 값에 덮어 씌워짐.
def Dictkeyupper(dicData):
    # dicDatadml 타입 확인
    if isinstance(dicData, dict):
        # key 값을 대문자로 바꾸는 부분, value값은 재귀함수
        return {k.upper(): Dictkeyupper(v) for k, v in dicData.items()}
    # 타입이 리스트면(value값이면)
    elif isinstance(dicData, list):
        # value값을 리스트화 하는 과정.
        return [Dictkeyupper(v) for v in dicData]
    # value값 하나하나 리스트에 찍음.
    else:
        return dicData


# key값을 전부 대분자로 바꾼 딕셔너리
upperDic = Dictkeyupper(menuDic)

while True:
    print("메뉴를 선택 하세요.")
    menu = input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : ")
    if menu == "1":
        for key in menuDic:
            print(key, ":", menuDic[key])
    elif menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력 하세요 : ")
        if rtrv_name in menuDic:
            print(menuDic[rtrv_name])
        else:
            print("찾는 메뉴가 없습니다.")
    elif menu == "3":
        add_name = input("추가 할 메뉴를 입력 하세요 : ")
        if add_name not in menuDic:
            grp = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("제품 설명 : ")
            menuDic[add_name] = [grp, price, desc]
        else:
            print("메뉴가 이미 존재 합니다.")
        for key in menuDic:
            print(key, ":", menuDic[key])
    elif menu == "4":
        del_name = input("삭제 할 메뉴를 입력 하세요 : ")
        if del_name in menuDic:
            del menuDic[del_name]
        else:
            print("삭제 할 메뉴가 없습니다.")
        for key in menuDic:
            print(key, ":", menuDic[key])
    elif menu == "5":
        print("영업을 종료 합니다.")
        break
