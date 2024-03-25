# 딕셔너리 : {}, 키와 값의 쌍으로 이루어져 있음, 자바의 HashMap 동일 구조
# 키와 값은 클론으로 구분
dict = {"정경수": 90, "고유림": 88, "나도희": 89}
print(dict.keys())
print(dict.values())
print(dict.items())
print("고유림" in dict)
print("안유진" in dict)

if "고유림" in dict:
    print(dict["고유림"])
