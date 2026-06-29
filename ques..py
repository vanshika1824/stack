#759816283
#516283
s = "759816283"
st = []
n = 3 
st.append(s[0])
res = ""

for i in range(1,len(s)):
    while n>0 and len(st)!= 0 and ord(st[-1])-ord('0') >= ord(s[i])-ord('0'):
        st.pop()
        n -= 1
    st.append(s[i])

for i in range(len(st)-1,-1,-1):
    res = st[i] + res

print(res)