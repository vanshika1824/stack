s = "{[([{}])]}"

st = []
balanced = True

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

for ch in s:
    if ch in "({[":
        st.append(ch)
    else:
        if len(st) == 0 or st.pop() != pairs[ch]:
            balanced = False
            break

if balanced and len(st) == 0:
    print("Balanced")
else:
    print("Not Balanced")