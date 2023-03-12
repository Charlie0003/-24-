# 这是第5次测试
from random import randint, uniform
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Main:
    def __init__(self):
        # 商品数量
        shop_num = 100
        shop_front_plus = 0.01
        # 测试次数
        exam_num = 1000000

        input_values = []
        successful_times = []
        # 商品最高值
        shop_max = 100
        # 商品最低值
        shop_min = 0
        # 商品策略前%?a个
        shop_front_low = 0
        shop_front_high = 100
        # True:randient False:uniform
        exam_kind = False

        shop_times = int((shop_front_high - shop_front_low) / shop_front_plus)
        for i in range(shop_times + 1):
            a, b = self.run(shop_num, shop_front_low, exam_num, shop_min, shop_max, exam_kind)
            input_values.append(a)
            successful_times.append(b)
            shop_front_low = round(shop_front_low + shop_front_plus, 2)
        self.draw_table(input_values, successful_times, shop_num,  exam_num)

    def run(self, shop_num, shop_front, exam_num, shop_min, shop_max, exam_kind):
        """主程序"""
        # 前百分之n的商品数量
        self.front_shops_num = int(shop_num * shop_front / 100)
        # 成功的次数，即选择了最优惠商品
        a = 0
        # 开始测试
        for i in range(exam_num):
            # 创建物品价值列表
            things_list = []
            # 获取前面与后面物品的列表
            self.set_up(things_list, shop_num, shop_min, shop_max, exam_kind)
            # 获取前面物品的最高值
            self.get_a_max()
            # 后面的物品更好就选它,获取最佳选择
            best_choose = self.choose_best()
            # 最佳选择与最优惠商品一样吗
            if self.best_shop == best_choose:
                # 一样,成功次数+1
                a += 1
        # 顺便将值也打印下
        print(shop_front)
        print(a)
        print()
        # 制作图表
        return shop_front, a

    def set_up(self, things_list, shop_num, shop_min, shop_max, exam_kind):
        """获取商品前后以及排列表格"""
        self.things_list, self.new_list = self.create_things(things_list, shop_num, shop_min, shop_max, exam_kind)
        # 商品前面的东西
        self.front_things_list = self.things_list[0: self.front_shops_num]
        # 商品后面的东西
        self.behind_things_list = self.things_list[self.front_shops_num:]

    def create_things(self, things_list, shop_num, shop_min, shop_max, exam_kind):
        """创建n个价值从1-100不等的商品"""
        for _ in range(shop_num):
            if exam_kind:
                thing = randint(shop_min, shop_max)
            else:
                thing = uniform(shop_min, shop_max)
            things_list.append(thing)
        new_list = sorted(things_list, reverse=True)
        self.best_shop = new_list[0]
        return things_list, new_list

    def get_a_max(self):
        """找到前面最高值"""
        self.front_things_list.sort(reverse=True)
        if len(self.front_things_list) > 0:
            self.max_shop = self.front_things_list[0]
        else:
            self.max_shop = 0

    def choose_best(self):
        """选择比最高还最高"""
        best_choose = 0
        for thing in self.behind_things_list:
            if thing > self.max_shop:
                best_choose = thing
                break
        if best_choose == 0 and len(self.behind_things_list) > 0:
            best_choose = self.behind_things_list[-1]
        return best_choose

    def draw_table(self, input_values, successful_times, shop_num, exam_num):
        """绘制图表"""
        print(input_values, successful_times)
        data = [Bar(x=input_values, y=successful_times)]
        x_axis_config = {'title': '策略百分比'}
        y_axis_config = {'title': '成功次数'}
        my_layout = Layout(title='购物概率',
                           xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({'data': data, 'layout': my_layout}, filename=f'{shop_num} {exam_num} uniform.html')


if __name__ == "__main__":
    main = Main()