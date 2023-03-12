from random import randint, randrange, choice, sample, shuffle, random, uniform
# randint：两个定值之间返回随机整数
print(randint(1, 10))
# randrange:第三个参数是产生的随机值之间的“增量”。默认值为1
print(randrange(1, 10, 2))
# choice:从？选择一个
dict1 = {1: 'apple', 2: 'pear', 3: 'banana'}
print(choice(dict1))
num = [2, 3, 5, 7, 11, 13, 17, 19]
print(choice(num))
name = 'ABCDHELLO'
print(choice(name))
# sample:随机样本
fruit = ['apple', 'cheery', 'pear', 'mango', 'pineapple', 'watermelon']
print(sample(fruit, k=2))
# shuffle:打乱列表(直接更新列表！)
shuffle(fruit)
print(fruit)
# random:随机函数,返回一个介于0.0和1.0之间的随机浮点值。
print(random())
# uniform:返回两个数字之间的随机浮点值
print(uniform(1, 100))