import speedtest

Speed = speedtest.Speedtest()
Speed.get_servers()

print('正在计算')

dowmload = Speed.download()
upload = Speed.upload()

print(f'下载速度{dowmload / 1024 / 1024:.2f}Mbits')
print(f'上传速度{upload / 1024 / 1024:.2f}Mbits')