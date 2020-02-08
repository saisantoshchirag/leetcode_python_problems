s = 'A man, a plan, a canal:Panama'
sr = ''
for i in s:
    if i.isalpha() or i.isnumeric():
        sr+=i.lower()
print(sr)
print(sr==sr[::-1])
