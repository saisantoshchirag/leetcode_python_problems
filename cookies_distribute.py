t=int(input())
for _ in range(t):
	n=int(input())
	sor_box = list(map(int, input().split()))
	sume=sum(sor_box)
	if sume%2==0:
		print("YES")
	else:
		print("NO")
