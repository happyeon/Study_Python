i = 1

while i <= 10:
    if i > 5:
        break       # break만나서 정상적으로 종료되지 않아서 else 부분이 출력되지 않는다.
    print(i)
    i += 1
else:
    print('i:', i)


print('------------')

for i in range(1, 10):
    if i%2 == 0:
        continue
    print(i)
else:
    print('i:', i)
