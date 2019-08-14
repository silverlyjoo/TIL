arr = [15616,879,4561,849,7567]
temp = [0]*(len(arr)+1)

def msort(s, e):
    if s >= e: return # 원소 하나 단위로 쪼갰으면 리턴
    m = (s+e) // 2
    msort(s, m) # 왼쪽 쪼개기
    msort(m+1, e) # 오른쪽 쪼개기

    l, r, t = s, m+1, s

    while l <= m and r <= e:
        if arr[l] < arr[r]: # 왼쪽 영역이 작으면 왼쪽 영역 값을 임시 버퍼로
            temp[t] = arr[l]
            t += 1
            l += 1

        else:
            temp[t] = arr[r] # 아니면 오른쪽 값을 임시 버퍼로
            t += 1
            r += 1
    while l <= m: # L쪽이 남은경우 그대로 버퍼에 넣기
        temp[t] = arr[l]
        t += 1
        l += 1

    while r <= e: # R쪽이 남은경우 그대로 버퍼에 넣기
        temp[t] = arr[r]
        t += 1
        r += 1

    for i in range(s, e+1): # 원본에 복사하기
        arr[i] = temp[i]

print(arr)
msort(0, len(arr)-1)

print(arr)