from itertools import permutations

a = int(input("请输入第1个数字:"))
b = int(input("请输入第2个数字:"))
c = int(input("请输入第3个数字:"))
d = int(input("请输入第4个数字:"))
my_list = [a, b, c, d]
# 对4个整数随机排列的列表
result = [c for c in permutations(my_list, 4)]

symbols = ["+", "-", "*", "/"]

list2 = []  # 算出24的排列组合的列表

flag = False

for one, two, three, four in result:
    for s1 in symbols:
        for s2 in symbols:
            for s3 in symbols:
                if s1 + s2 + s3 == "+++" or s1 + s2 + s3 == "***":
                    express = ["{0}{1}{2}{3}{4}{5}{6}".format(one, s1, two, s2, three, s3, four)]  # 全加或者乘时，括号已经没有意义。
                else:
                    express = ["(({0}{1}{2}){3}{4}){5}{6}".format(one, s1, two, s2, three, s3, four),
                               "({0}{1}{2}){3}({4}{5}{6})".format(one, s1, two, s2, three, s3, four),
                               "(({0}{1}({2}{3}{4})){5}{6})".format(one, s1, two, s2, three, s3, four),
                               "{0}{1}(({2}{3}{4}){5}{6})".format(one, s1, two, s2, three, s3, four),
                               "{0}{1}({2}{3}({4}{5}{6}))".format(one, s1, two, s2, three, s3, four)]

                for e in express:
                    try:
                        # if eval(e) == 24:
                        if round(eval(e), 6) == 24:
                            list2.append(e)
                            flag = True
                    except ZeroDivisionError:
                        pass

list3 = set(list2)  # 去除重复项
for c in list3:
    print(c)
print(len(list3))

if not flag:
    print("NO！")