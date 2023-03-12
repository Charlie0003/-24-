from itertools import permutations, product


def calc_24(nums):
    results = set()
    for a, b, c, d in permutations(nums):
        # 1. 三个数的运算
        for op1, op2, op3 in product(['+', '-', '*', '/'], repeat=3):
            try:
                res1 = eval(f"(({a} {op1} {b}) {op2} {c}) {op3} {d}")
                if res1 == 24:
                    results.add(f"(({a} {op1} {b}) {op2} {c}) {op3} {d}")
            except:
                pass

            try:
                res2 = eval(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
                if res2 == 24:
                    results.add(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
            except:
                pass

        # 2. 两个数的运算
        for op1, op2, op3 in product(['+', '-', '*', '/'], repeat=3):
            try:
                res3 = eval(f"{a} {op1} (({b} {op2} {c}) {op3} {d})")
                if res3 == 24:
                    results.add(f"{a} {op1} (({b} {op2} {c}) {op3} {d})")
            except:
                pass

            try:
                res4 = eval(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
                if res4 == 24:
                    results.add(f"({a} {op1} {b}) {op2} ({c} {op3} {d})")
            except:
                pass

            try:
                res5 = eval(f"({a} {op1} {b}) {op2} {c} {op3} {d}")
                if res5 == 24:
                    results.add(f"({a} {op1} {b}) {op2} {c} {op3} {d}")
            except:
                pass

            try:
                res6 = eval(f"{a} {op1} ({b} {op2} ({c} {op3} {d}))")
                if res6 == 24:
                    results.add(f"{a} {op1} ({b} {op2} ({c} {op3} {d}))")
            except:
                pass

    return len(results)


a2 = set()
new_list = []
for a in range(1, 14):
    for b in range(1, 14):
        for c in range(1, 14):
            for d in range(1, 14):
                my_list = [a, b, c, d]
                my_list.sort(key=None, reverse=True)
                if f'{my_list}' not in a2:
                    a2.add(f'{my_list}')
                    possible = calc_24(my_list)
                    list = [my_list, possible]
                    print(a, b)
                    new_list.append(list)
print(new_list)
