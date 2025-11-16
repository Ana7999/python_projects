text = input()

a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0

for ch in text:
    if ch == "a":
        sum += a
    if ch == "e":
        sum += e
    if ch == "i":
        sum += i
    if ch == "o":
        sum += o
    if ch == "u":
        sum += u
print(sum)