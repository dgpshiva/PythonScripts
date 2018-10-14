def calculateSpan(price):
    n = len(price)

    S = [0 for i in range(0, n)]
    S[0] = 1

    st = []
    st.append(0)

    for i in range(1, n):
        while len(st) > 0 and price[st[len(st) - 1]] <= price[i]:
            st.pop()

        S[i] = i+1 if len(st)==0 else i-st[len(st)-1]

        st.append(i)

    return S


price = [10, 4, 5, 90, 120, 80]

# Fill the span values in array S[]
S = calculateSpan(price)

# Print the calculated span values
for i in range(0, len(S)):
    print S[i],

