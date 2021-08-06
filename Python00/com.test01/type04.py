# tuple : list와 거의 같다.  (tuple 많이 쓰임 중요함)

# 생성자 사용
a = tuple()
print(a)
b = tuple([1, 2, '3'])
print(b)

# 튜플은 값을 변경(추가, 수정, 삭제)할 수 없다.
# a.append(1)
# b[1] = '2'

# () 사용
d = tuple(range(3, 6))
print(d)
print(b + d)

# tuple -> list
e = list(d)
e.append(6)
print(e)

# list -> tuple
f = tuple(e)
print(f)

# unpacking (갯수만큼 안해주면 에러남, _를 써서 날릴 수도 있음)
g, h, i, j = f
print(g)
print(h)
print(i)
print(j)