def manacher(s):
    s = "#" + "#".join(s)+'#'
    RL = [0]*len(s)
    MaxRight = 0
    pos = 0
    Maxlen = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2*pos - i], MaxRight - i)
        else:
            RL[i] = 1
        while i - RL[i] >= 0 and i+RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
            RL[i] += 1
        if RL[i]+i-1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        Maxlen = max(Maxlen, RL[i])
    mid = RL.index(max(RL))
    return s[ mid - RL[mid] + 1: mid + RL[mid]].replace("#", "")

print(manacher("abba"))
print