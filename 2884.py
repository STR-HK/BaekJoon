inp = input().split(' ')

H = int(inp[0])
M = int(inp[1])

M -= 45
if M < 0:
    H -= 1
    M += 60
if H < 0:
    H = 23

print(H, M)