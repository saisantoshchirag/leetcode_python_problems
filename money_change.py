
n = int(input())
coins = 0
den = [10,5,1]
for i in range(3):
    coins += n//den[i]
    n %= den[i]
print(coins)
x = sorted(den)
