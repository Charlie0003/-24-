from PIL import Image, ImageFilter


# image = Image.open(x) 打开x图片
image = Image.open('1000.png')
# rect = a, b, c, d (左上角x坐标，左上角y坐标，右下角x坐标，右下角y坐标)
rect = 790, 369, 881, 393
# crop(rect) 按照rect将image剪
image = image.crop(rect)
# image.save('x') 保存到x
image.save('E:\\录屏视频\\new.png')
# 新尺寸
size = 2880, 1800
# 将尺寸改为size
image.thumbnail(size)
# 展示图片
image.show()
# 逆时针旋转90度
image = image.rotate(90)
# 左右翻转
image = image.transpose(Image.FLIP_LEFT_RIGHT)
# 添加长方形在图片上
for x in range(80, 310):
    for y in range(20, 360):
        # image.putpixel((坐标), (颜色))
        image.putpixel((x, y), (128, 128, 128))
# 滤镜
image = image.filter(ImageFilter.CONTOUR)
# 输出图片格式
format = image.format
# 输出图片分辨率
size = image.size