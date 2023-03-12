from itertools import permutations, product
from time import time

def calc_24(nums, need_result):
    results = set()
    for a, b, c, d in permutations(nums):
        # 1. 三个数的运算
        for op1, op2, op3 in product(['+', '-', '*', '/'], repeat=3):
            try:
                res1 = eval(f"(({a} {op1} {b}) {op2} {c}) {op3} {d}")
                if res1 == need_result:
                    return True
            except:
                pass

            try:
                res2 = eval(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
                if res2 == need_result:
                    return True
            except:
                pass

        # 2. 两个数的运算
        for op1, op2, op3 in product(['+', '-', '*', '/'], repeat=3):
            try:
                res3 = eval(f"{a} {op1} (({b} {op2} {c}) {op3} {d})")
                if res3 == need_result:
                    return True
            except:
                pass

            try:
                res4 = eval(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
                if res4 == need_result:
                    return True
            except:
                pass

            try:
                res5 = eval(f"({a} {op1} {b}) {op2} {c} {op3} {d}")
                if res5 == need_result:
                    return True
            except:
                pass

            try:
                res6 = eval(f"{a} {op1} ({b} {op2} ({c} {op3} {d}))")
                if res6 == need_result:
                    return True
            except:
                pass
    return False





y_ray = []
for results in range(0,1):
    a = set()
    b = []
    alls = 0
    start = time()
    for i in range(1, 14):
        for j in range(1, 14):
            for k in range(1, 14):
                for l in range(1, 14):
                    m = [i,j,k,l]
                    m.sort(key=None, reverse=True)
                    b.append(m)
                    if f'{m}' not in a:
                        if calc_24(m, results):
                            alls+=1
                        a.add(f'{m}')
    print('-'*200)
    print(alls)
    p = alls/len(a)
    print(p)
    y_ray.append(p)
    print(f'cost:{time() - start}')


print(y_ray)