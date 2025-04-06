# i = 1
# res = []
# while i <= 1000000:
#     res.append(i)
#     i*=7
# print(res)

summ=100_0000

for a in range(0, 6):
    for b in range(0, 6):
        for c in range(0, 6):
            for d in range(0, 6):
                for e in range(0, 6):
                    for f in range(0, 6):
                        for g in range(0, 6):
                            for h in range(0, 6):
                                if a+b*7+c*49+d*343+e*2401+f*16807+g*117649+h*823543==summ:
                                    print(a+b+c+d+e+f+g+h)