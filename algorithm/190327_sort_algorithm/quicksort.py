

def qsort(s, e):

    if s >= e: return
    p, t = e, s
    for l in range(s, e):
        if a[l] < a[p]:
            a[l], a[t] = a[t], a[l]
            t += 1
    a[t], a[p] = a[p], a[t]
    qsort(s, t-1)
    qsort(t+1, e)








a = [1564,49,7865,15,849779,451]
print(a)
qsort(0,len(a)-1)
print(a)