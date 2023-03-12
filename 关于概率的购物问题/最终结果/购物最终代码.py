# 导入随机数
from random import randint, uniform
# 导入购物的变量
import shop_numbers as c
import matplotlib.pyplot as plt


class Main:
    def __init__(self):
        self.run()

    def run(self):
        """主程序"""
        # 这两个值是列表纵横值
        input_values = []
        successful_times = []
        # 从百分之1试到百分之99
        for j in range(98):
            # 前百分之n的商品数量
            self.front_shops_num = int(c.shop_num * (c.shop_front + j) / 100)
            # 成功的次数，即选择了最优惠商品
            a = 0
            # 开始测试
            for i in range(c.exam_num):
                # 创建物品价值列表
                things_list = []
                # 获取前面与后面物品的列表
                self.set_up(things_list)
                # 获取前面物品的最高值
                self.get_a_max()
                # 后面的物品更好就选它,获取最佳选择
                best_choose = self.choose_best()
                # 最佳选择与最优惠商品一样吗
                if self.is_or_not_best(best_choose):
                    # 一样,成功次数+1
                    a += 1
            # 将百分之n横坐标扔进来
            input_values.append(j + 1)
            # 把成功次数纵坐标扔进来
            successful_times.append(a)
            # 顺便将值也打印下
            print(j + 1)
            print(a)
            print()
        # 制作图表
        self.draw_table(input_values, successful_times)

    def set_up(self, things_list):
        """获取商品前后以及排列表格"""
        self.things_list, self.new_list = self.create_things(things_list)
        # 商品前面的东西
        self.front_things_list = self.things_list[0: self.front_shops_num]
        # 商品后面的东西
        self.behind_things_list = self.things_list[self.front_shops_num:]

    def create_things(self, things_list):
        """创建n个价值从1-100不等的商品"""
        for _ in range(c.shop_num):
            if c.exam_kind:
                thing = randint(c.shop_min, c.shop_max)
            else:
                thing = uniform(c.shop_min, c.shop_max)
            things_list.append(thing)
        new_list = sorted(things_list, reverse=True)
        self.best_shop = new_list[0]
        return things_list, new_list

    def get_a_max(self):
        """找到前面最高值"""
        self.front_things_list.sort(reverse=True)
        self.max_shop = self.front_things_list[0]

    def choose_best(self):
        """选择比最高还最高"""
        best_choose = 0
        for thing in self.behind_things_list:
            if thing > self.max_shop:
                best_choose = thing
                break
        if best_choose == 0:
            best_choose = self.behind_things_list[-1]
        return best_choose

    def is_or_not_best(self, best_choose):
        """判断是否是最佳选择"""
        if self.best_shop == best_choose:
            return True
        else:
            return False

    def draw_table(self, input_values, successful_times):
        """绘制图表"""
        fig, ax = plt.subplots()
        ax.plot(input_values, successful_times, linewidth=3)
        # 保存至桌面
        plt.savefig("E:\\table.png")
        # 展示下
        plt.show()


if __name__ == "__main__":
    main = Main()