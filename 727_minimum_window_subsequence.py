import sys
S="abcdebdde"
T = "bde"

#S="fweekpamjwqobhxiesgzivminqqjjkgnhkdxpfjvvgfcdlgwvwtdwizpjcuwnwpioxcshyjglqjnkluedopzyhozjzqnjentspwffoawwbgyhrrapncwetqulmaupkkwugkpfztgejujlakrnkvefbvncfzhhmciztzjzrzrzlcfkejmlkhlogtraexhgrvxitcnaacegjrkwbseomwvdawsymemhsvtqcpbfvinhngdvhnrswwgoff"
#T="qkkwtlzbbn"
#S="fweekpamjwqobhxiesgzivminqqjjkgnhkdxpfjvvgfcdlgwvwtdwizpjcuwnwpioxcshyjglqjnkl"
#T="qk"

col = len(S)
row = len(T)
f = [0]*(col+1)
g = [0]*(col+1)
b = 0
tmp = f[0]
for i,tc in enumerate(T):
    g = f
    f = [0]*(col+1)
    valid = S[b:].find(tc)
    if valid == -1:
        print ""
    b+=(valid)
    print b
    for j, sc in enumerate(S[b:]):
        j = j + b
        jj = j+1
        if sc == tc:
            f[jj] = g[jj-1] +1
        else:
            f[jj] = f[jj-1] +1
    b += 1

    print "find:"+ tc
    print f
    print b
    print S[b:]
    print f[b:]

flag = 0
m = 100000
for i,n in enumerate(f[b:]):
    if n < m:
        m = n
        flag = i
end = flag+b
begin = end - m+1
print S[begin-1:end]
