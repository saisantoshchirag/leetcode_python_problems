text = "we will we will rock you"
first = "we"
second = "will"
text = text.split()
print(text)
out = []
for i in range(len(text)-2):
    if text[i] == first and text[i+1]==second:
        out.append(text[i+2])
print(out)
        
