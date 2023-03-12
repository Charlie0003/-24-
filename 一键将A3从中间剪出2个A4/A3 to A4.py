import os
from PIL import Image

# path定义要获取的文件名称的目录
path = "E:\\待处理A3\\"

# os.listdir()方法获取文件夹名字，返回数组
file_name_list = os.listdir(path)

# 在桌面生成文件，有就不建
if not os.path.isdir("E:\\处理后A4"):
    os.mkdir("E:\\处理后A4")
# 文件名的名称变量
a = 1

for name in file_name_list:
    # 获取文件绝对路径
    file_location = f"{path}{name}"
    # 打开文件
    image = Image.open(file_location)
    # 获取图片尺寸
    size = image.size

    # 剪辑尺寸
    rect = 0, 0, size[0] / 2, size[1]
    rect2 = size[0] / 2, 0, size[0], size[1]

    # crop(rect) 按照rect将image剪
    image1 = image.crop(rect)
    image2 = image.crop(rect2)

    # image.save('x') 保存到x
    image1.save(f'E:\\处理后A4\\{a}{os.path.splitext(name)[1]}')
    a += 1
    image2.save(f'E:\\处理后A4\\{a}{os.path.splitext(name)[1]}')
    a += 1
