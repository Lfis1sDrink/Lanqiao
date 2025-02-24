""""
lanqiao0569249167|L242|2022-03-21 00:37
89991231为输入 可以得到90011009和90900909 只是说输入最大为89991231可没说输出最大为89991231噢，看清楚题
"""
month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["01","02","03","04","05","06","07","08","09","10","11","12",
       "13","14","15","16","17","18","19","20","21","22","23","24",
       "25","26","27","28","29","30","31"]


date_input = input()
year_begin = int(date_input[:4])
flag1,flag2 = 0,0

#找第一个回文数
for year in range(year_begin,8999):
    for m in range(12):
        for d in range(31):
            date = str(year)+month[m]+day[d]
            if (date[:4]==date[4:][::-1]):
                if (int(date) > int(date_input)):
                    print(int(date))
                    flag1 = 1
                    break
        if flag1 == 1:
            break
    if flag1 == 1:
        break


#找第一个ABABBABA回文数
for year in range(year_begin,8999):
    for m in range(12):
        for d in range(31):
            date = str(year)+month[m]+day[d]
            if ( date[:2]==date[2:4] and date[:4]==date[4:][::-1]):
                if (int(date) > int(date_input)):
                    print(int(date))
                    flag2 = 1
                    break
        if flag2 == 1:
            break
    if flag2 == 1:
        break