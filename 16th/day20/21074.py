from datetime import datetime

timelist = []
with open("D:\\Document\\Code\\Lanqiao\\16th\\day20\\records.txt","r") as file:
    for line in file:
        date,time = line.split()
        time = date+" "+time
        dt = datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
        timeStamp = datetime.timestamp(dt)
        timelist.append(timeStamp)


timelist.sort()
print(timelist)
ans = 0
for i in range(0,len(timelist),2):
    ans += timelist[i+1] - timelist[i]


print(ans)