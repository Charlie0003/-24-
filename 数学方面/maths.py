class maths:
    def fenjiesuyinshu(self, number):
        """分解素因数"""
        if int(number) == number and number >= 2:
            yinzis = []  # 将所有因子储存在这里
            for yinzi in range(2, number):
                while number % yinzi == 0:
                    yinzis.append(yinzi)
                    number /= yinzi
        return yinzis

    def kaigenhao(self, number):
        """开根号"""
        # 超过九位会特别慢
        number_old = number
        if int(number) == number and number >= 9:
            b = 1
            for yinzi in range(2, int(number * 1/2) + 1):
                a = 0
                while number % yinzi == 0:
                    number /= yinzi
                    a += 1
                    if a == 2:
                        b *= yinzi
                        a = 0

        number_outside = b
        number_inside = int(number_old / (b * b))
        return f'{number_outside} {number_inside}'


maths = maths()
b = maths.kaigenhao()
print(b)


