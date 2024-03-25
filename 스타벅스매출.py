fileName = "스타벅스일일매출.txt"
with open(fileName,"r",encoding="utf-8") as F:
    # for line in F:
    #     print(line, end="")
    header = F.readline()
    headerList = header.split()
    espresso = []
    americano =[]
    cafelatte = []
    cappucino =[]
    for line in F:
        dataList = line.split()
        espresso.append(int(dataList[1]))
        americano.append(int(dataList[2]))
        cafelatte.append(int(dataList[3]))
        cappucino.append(int(dataList[4]))
    print(f"{headerList[1]} 전체판매량 : {sum(espresso)}, 일평균 판매량 : {sum(espresso)/len(espresso)}")
    print(f"{headerList[2]} 전체판매량 : {sum(americano)}, 일평균 판매량 : {sum(americano)/len(americano)}")
    print(f"{headerList[3]} 전체판매량 : {sum(cafelatte)}, 일평균 판매량 : {sum(cafelatte)/len(cafelatte)}")
    print(f"{headerList[4]} 전체판매량 : {sum(cappucino)}, 일평균 판매량 : {sum(cappucino)/len(cappucino)}")

    # for line in F:
    #     dataList = line.split()
    #     print(dataList)