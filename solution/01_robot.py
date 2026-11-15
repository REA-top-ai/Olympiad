dx = [0,1,0,-1]
dy = [1,0,-1,0]
x=y=d=0
#T_T kapec
s = input()
i = 0
while i < len(s):
    if s[i] in 'FRBL':
        t = (d+'FRBL'.index(s[i]))%4
        x += dx[t]
        y += dy[t]
    elif s[i] == ')':
        d = (d + 1) % 4
    elif s[i] == '(':
        d = (d + 3) % 4
    elif s[i].isdigit():
        k = int(s[i])
        end = s.find(']', i)
        s = s[:i]+ s[i+2:end]*k + s[end+1:]
        continue
    i +=1
print(x,y)