noList = [i+1 for i in range(2000)]
ansList = []
iptList = []
timeList = []

maxComboTime = 0

with open(f"D:\\Document\\Code\\Lanqiao\\16th\\day15\\log.txt", 'r') as file:
    for line in file:
        ans, ipt, time = map(str, line.split())
        time = int(time)
        ansList.append(ans)
        iptList.append(ipt)
        timeList.append(time)

i,j,combotime = 0,0,0
while i < 2000:
    if ansList[i] == iptList[i]:
        j = i+1
        while j < 2000:
            if ansList[i] != iptList[i]:
                break
            if timeList[j] - timeList[i]:
                break
            #用Excel做了
        


