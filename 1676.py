N = int(input())

pac = 1

for i in range(N):
    pac *= (N - i)

le = 0

for p in range(len(str(pac))):
    if str(pac)[-(p + 1)] == '0':
        le += 1
    else:
        break
print(le)