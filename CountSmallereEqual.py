lst = [100,80,60,70,60,75,80]

res = []
st = []

for i in range(0,len(lst)):
    curr = lst[i]
    temp = []
    c = 1
    while len(st)!=0:
        if curr>=st[-1]:
            c+=1
            temp.append(st.pop())
        else:
            break
    res.append(c)
    st.append(curr)
    temp.reverse()
    st.extend(temp)
print(res)