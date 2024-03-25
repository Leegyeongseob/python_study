# ***각 사이트 비밀번호 자동으로 만들기***
# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 +글자에 포함된 'k' 갯수+ '!' + 자신의이니셜(예: 'jks')
file_name = 'pwd.txt'
f = open(file_name,"wt",encoding = "UTF-8")
while True:
    addr = input("사이트 : ")
    if addr == "exit": break
    store_str = addr.replace("http://", "")#리플레이스
    store_str = store_str[:store_str.index(".")] #슬라이싱
    pwd = store_str[:3] + str(len(store_str)) + str(store_str.count("o"))+str(store_str.count("k"))+"lgs"
    f.write(pwd + "\n")
f.close()