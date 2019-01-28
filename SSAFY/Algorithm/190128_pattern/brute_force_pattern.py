def Bruteforce(p,t):
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(p): return i-len(p)
    else: return -1

p = "is"
t = "Thasdfis is a book~!"
print(Bruteforce(p, t))
print(t.count('is'))
