def func01(x, y):
    return x + y

def func02(x, y):
    return x+y, x-y

def func03(x, y):
    print('{}, {} 두 개가 입력되었습니다.'.format(x, y))
    print('%d + %d = %d'%(x, y, x+y))

if __name__ == '__main__':
    print(func01(1, 3))
    print(func02(4, 7))     # 튜플로 출력 (일반적으로 값이 여러개일 경우에는 튜플로 출력됨)
    func03(6, 8)