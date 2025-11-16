import sys
from sys import maxsize

n = input()
# promenljiva koja cuva vrednost najveceg trenutnog broja
max_n = -sys.maxsize

while n != "Stop":
    current_n = int(n)
    if current_n > max_n:
        max_n = current_n
    n = input()
print(max_n)
