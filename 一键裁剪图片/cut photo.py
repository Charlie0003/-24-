from PIL import Image

names = []
path = "E:\\截图或视频"
file_path = f'{path}\\文件list.txt'   # 1
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    names.append(line.strip())

for name in names:
    path_photo = f'{path}\\{name}'
    image = Image.open(path_photo)
    rect = 598, 309, 989, 346
    image = image.crop(rect)
    image.save(f'E:\\123\\{name}')