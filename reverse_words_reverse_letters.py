string = "Let's take LeetCode contest"

string = string[-1::-1].split()

print(string)
string = list(reversed(string))
print(string)
s = ' '.join(string)
print(s)
