date = "20019-12-18"
day = list(map(int, date.split('-')))
if day[0]%4==0:
    if day[0]%100==0:
        if day[0] % 400==0:
            feb = 29
        else:
            feb = 28
    else:
        feb = 29
else:
    feb = 28
months = [31,feb,31,30,31,30,31,31,30,31,30,31]
print(sum(months[:day[1]-1])+day[-1])
months1 = {1:31,2:feb,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
print(months1)
n = 0
for i in range(day[1]-1):
    n += months1[i+1]
print(n+day[-1])
