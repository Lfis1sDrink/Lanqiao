from datetime import datetime


T = int(input())
for i in range(T):
  year, time, x = input().split()
  timeStr = year + " " + time
  dt = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
  timeStamp = datetime.timestamp(dt)
  timeGap = timeStamp-(3600*8) % (int(x)*60)
  timeStamp = timeStamp - timeGap

  time = datetime.fromtimestamp(timeStamp)
  print(time)