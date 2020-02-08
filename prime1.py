def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    f = 1
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            return False
    return True
def find_key(encryption_key):
    num = int(encryption_key,16)
    fa = [i for i in range(2,1+(num//2)) if num%i==0 and (isPrime(i)) and isPrime(num//i)]
    return (fa[0]-1)*(fa[1]-1)   
print(find_key('2533'))
