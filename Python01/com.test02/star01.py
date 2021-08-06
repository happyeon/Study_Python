'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
print('-------')

for i in range(5):
    print('*' * (i + 1))
print('--------')



'''
*****
****
***
**
*
'''
# 내코드
for i in range(5, 0, -1):
    print('*' * i)
print('--------')

# 쌤코드
for i in range(5):
    print('*' * (5-i))
print('--------')


'''
    *
   **
  ***
 ****
*****
'''
# 내코드
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print('--------')

# 쌤코드
for i in range(5):
    print(' ' * (4-i) + '*' * (i+1))
print('--------')


'''
*****
 ****
  ***
   **
    *
'''
# 내코드
for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print('--------')

# 쌤코드
for i in range(5):
    print(' ' * i + '*' * (5-i))
print('--------')

'''
    *
   ***
  *****
 *******
*********
'''
# 내코드
for i in range(1, 6):
    for j in range(6-i):
        print(' ', end='')
    for j in range(2*i - 1):
        print('*', end='')
    print()
print('--------')

# 쌤코드
for i in range(5):
    print(' ' * (4-i) + '*' * (2*i + 1))