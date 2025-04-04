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

logList = []
with open(f"D:\\Document\\Code\\Lanqiao\\16th\\day15\\log.txt",'r') as file:
    for line in file:
        correct,iput,time = line.split()
        time = int(time)
        # if correct == iput:
        logList.append((correct,iput,time))

startCombo = 2709446165404
combo = 0
comboTimes = 0

for i in range(1,len(logList)):
    
    if logList[i][0] == logList[i][1]:
        combo += 1
        if logList[i][2] - logList[i-1][2] <= 1000:
            continue
    else:
        comboTimes = max(combo,comboTimes)
        combo = 0

print(comboTimes)