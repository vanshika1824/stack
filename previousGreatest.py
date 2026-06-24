lst = [5, 7, 1, 2, 10, 9]

ans = []
st = []

for i in range(len(lst)):

    curr = lst[i]

    while len(st) != 0:
        if curr <st[-1]:
            ans.append(st[-1])
            st.append(curr)
            break
        st.pop()

    if len(st) == 0:
        ans.append(-1)
        st.append(curr)

print(ans)