from random import uniform
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Main:
    def __init__(self):
        shop_num = 10
        exam_num = 100
        b2 = True

        input_values, successful_times, shop_max, shop_min, shop_front_low, shop_front_high = [], [], 100, 0, 0, 100
        shop_front_plus = (shop_front_high - shop_front_low) / shop_num
        shop_times = int((shop_front_high - shop_front_low) / shop_front_plus) + 1
        for i in range(shop_times):
            a, b = self.run(shop_num, shop_front_low, exam_num, shop_min, shop_max, b2)
            input_values.append(a)
            successful_times.append(b)
            shop_front_low = round(shop_front_low + shop_front_plus, 2)
        self.draw_table(input_values, successful_times, shop_num,  exam_num)

    def run(self, shop_num, shop_front, exam_num, shop_min, shop_max, b):
        self.front_shops_num = int(shop_num * shop_front / 100)
        a = 0
        for i in range(exam_num):
            self.set_up(shop_num, shop_min, shop_max)
            self.get_a_max()
            best_choose = self.choose_best()
            if self.best_shop == best_choose:
                a += 1
        if b:
            print(shop_front)
            print(a)
            print()
        return shop_front, a

    def set_up(self, shop_num, shop_min, shop_max):
        self.things_list, self.new_list = self.create_things(shop_num, shop_min, shop_max)
        self.front_things_list = self.things_list[0: self.front_shops_num]
        self.behind_things_list = self.things_list[self.front_shops_num:]

    def create_things(self, shop_num, shop_min, shop_max):
        things_list = [round(uniform(shop_min, shop_max), 2) for _ in range(shop_num)]
        new_list = sorted(things_list, reverse=True)
        self.best_shop = new_list[0]
        return things_list, new_list

    def get_a_max(self):
        self.front_things_list.sort(reverse=True)
        if len(self.front_things_list) > 0:
            self.max_shop = self.front_things_list[0]
        else:
            self.max_shop = 0

    def choose_best(self):
        best_choose = 0
        for thing in self.behind_things_list:
            if thing > self.max_shop:
                best_choose = thing
                break
        return best_choose

    def draw_table(self, input_values, successful_times, shop_num, exam_num):
        data = [Bar(x=input_values, y=successful_times)]
        x_axis_config = {'title': '策略百分比'}
        y_axis_config = {'title': '成功次数'}
        my_layout = Layout(title='购物概率',
                           xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({'data': data, 'layout': my_layout}, filename=f'{shop_num} {exam_num} uniform.html')


if __name__ == "__main__":
    main = Main()