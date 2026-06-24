lst = [5,7,1,2,10,9]

#10
#[7,10,2,10,-1,-1]

ans = []
st = []
for i in range(len(lst)-1,-1,-1):
    while(len(st)!=0):
        curr = lst[i]
        if curr<st[-1]:
            ans.append(st[-1])
            st.append(curr)
            break
        else:
            st.pop()
    if len(st)==0:
        ans.append(-1)
        st.append(lst[i])
  
ans.reverse()
print(ans)  
