# 导入os模块
import os

# path定义要获取的文件名称的目录
path = "E:\\截图或视频"

# os.listdir()方法获取文件夹名字，返回列表
file_name_list = os.listdir(path)

# 转为转为字符串
file_name = str(file_name_list)

# replace替换"["、"]"、"'"
file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n")

# 创建并打开文件list.txt
f = open(path + "\\" + "文件list.txt", "w")

# 将文件下名称写入到"文件list.txt"
f.write(file_name)


"""import os

file_dir = "E:\\截图或视频"

path = os.walk(file_dir)
lst = []

for i in os.walk(file_dir):
    for j in i[2]:
        lst.append(j)

# 创建并打开文件list.txt
f = open(f"{file_dir}\\文件list.txt", "w")

# 将文件下名称写入到"文件list.txt"
f.write(str(lst))"""