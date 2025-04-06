# noList = [i+1 for i in range(2000)]
# ansList = []
# iptList = []
# timeList = []

# maxComboTime = 0

# with open(f"D:\\Document\\Code\\Lanqiao\\16th\\day15\\log.txt", 'r') as file:
#     for line in file:
#         ans, ipt, time = map(str, line.split())
#         time = int(time)
#         ansList.append(ans)
#         iptList.append(ipt)
#         timeList.append(time)

# i,j,combotime = 0,0,0
# while i < 2000:
#     if ansList[i] == iptList[i]:
#         j = i+1
#         while j < 2000:
#             if ansList[i] != iptList[i]:
#                 break
#             if timeList[j] - timeList[i]:
#                 break
#             #用Excel做了
        

# 2025年4月4日 重新做一遍
# 没做对

# logList = []
# with open(f"D:\\Document\\Code\\Lanqiao\\16th\\day15\\log.txt",'r') as file:
#     for line in file:
#         correct,iput,time = line.split()
#         time = int(time)
#         # if correct == iput:
#         logList.append((correct,iput,time))

# startCombo = 2709446165404
# combo = 0
# comboTimes = 0

# for i in range(1,len(logList)):
    
#     if logList[i][0] == logList[i][1]:
#         combo += 1
#         if logList[i][2] - logList[i-1][2] <= 1000:
#             continue
#     else:
#         comboTimes = max(combo,comboTimes)
#         combo = 0

# print(comboTimes)


# 2025年4月6日 再做一遍
# 做对了

logList = []

with open(f"D:\\Document\\Code\\Lanqiao\\16th\\day15\\log.txt",'r') as file:
    for line in file:
        correct,iput,time = line.split()
        time = int(time)
        # if correct == iput:
        logList.append((correct,iput,time))

comboTimes = 0
comboLog = []

#从第二个输入开始判断
for i in range(1,len(logList)):
    if logList[i][0] == logList[i][1] and logList[i][2] - logList[i-1][2] <= 1000:
        comboTimes += 1
    elif logList[i][0] == logList[i][1]:
        comboTimes = 1
    else:
        comboTimes = 0
    comboLog.append(comboTimes)

ans = 0
for i in range(len(comboLog)):
    ans = max(ans, comboLog[i])

print(ans)


"""
#从第二个输入开始判断

1172	b	r	1709447005955 	0
1173	w	o	1709447007243 	0
1174	o	o	1709447008088 	1
1175	w	w	1709447009458 	1
1176	n	n	1709447010090 	2
1177	n	n	1709447010194 	3
1178	o	o	1709447010692 	4
1179	y	y	1709447010868 	5
1180	k	k	1709447011260 	6
1181	w	w	1709447011577 	7
1182	i	i	1709447011604 	8
1183	y	y	1709447011782 	9
1184	q	p	1709447012742 	0
1185	d	d	1709447012850 	1

"""