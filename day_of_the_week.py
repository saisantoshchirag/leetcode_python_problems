def isleap(year):
    if year%4==0:
        if year%100==0:
            if year % 400==0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
day,m,year = 26,2,2068
ndays = 0
for i in range(1971,year):
    ndays += 365
    ndays += isleap(i)
months1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for j in range(1,m):
    ndays += months1[j]
ndays = ndays + isleap(year) + day
days = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
print(days[ndays%7])
