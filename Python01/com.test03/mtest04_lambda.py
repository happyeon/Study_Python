hap01 = lambda a, b: a + b
print(hap01(10, 20))

hap02 = lambda a, b, c: a + b + c
print(hap02(30, 40, 50))

gob = lambda a, b: a*b
print(gob(12, 34))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
print(a)
a.sort(key=lambda a: a[1])
print(a)

min01 = lambda x, y: x if x < y else y      # 참 if문 else 거짓
min02 = (lambda x, y: x if x < y else y)(33, 44)
print(min01(33, 44))
print(min02)

max01 = lambda x, y: x if x > y else y
print(max01(55,66))

b = lambda x: (lambda newx: x + newx)
print(b(100)(200))
c = b(100)
# c = lambda newx: 100 + newx
print(c)
d = c(200)
print(d)

# 1 ~ 100 사이의 5의 배수 출력
e = lambda x: bool(x % 5)
five = [i for i in range(1, 101) if not e(i)]
print(five)

f = lambda x: x if (x % 5 != 0) else None       # None은 false, null과 비슷한 느낌
res = [i for i in range(1, 101) if not f(i)]
print(res)

result = [i for i in range(1, 101) if not (lambda x: x if(x % 5 != 0) else None)(i)]
print(result)

#lambda : 함수를 직접 선언하는 것이 아니라 필요할 때 익명함수로 만들어서 일회용으로 사용