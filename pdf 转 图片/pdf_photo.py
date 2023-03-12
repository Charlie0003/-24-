# 导入这个库：python-office，简写为office
import os
import office

os.chdir('E:\\A3_to_A4.exe')

pdf_path = input('请输入PDF名')
if pdf_path == '':
    pdf_path = 1
# 一行代码，实现转换
office.pdf.pdf2imgs(
    pdf_path=f'E:\\{pdf_path}.pdf',
    out_dir='E:\\待处理A3'
)
# 参数说明：
# pdf_path = 你的PDF文件的地址
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址
a=input()