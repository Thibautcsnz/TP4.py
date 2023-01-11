m = [5, 2, 4, 8, 1, 3]
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] > m[j]:
            m[i], m[j] = m[j], m[i]
m.sort(reverse=True)
print(m)

#tab.sort agit sur la liste