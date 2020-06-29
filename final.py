count = 0
n = input()
s = input()
q = input()

while q > 0:
    count = 0
    a = input()
    for i in s[0, a-1]:
        if i == 'a-1':
            count = count + 1


print(count)
