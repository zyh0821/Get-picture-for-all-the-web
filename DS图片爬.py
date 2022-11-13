import time
from DrissionPage import MixPage


url = input('请输入网址：')
# https://www.umei.cc/bizhitupian/meinvbizhi/
scroll_time = input('请输入滚动加载时间：')
web = MixPage('d')
web.get(url)
time.sleep(1)
start = time.time()
img = []
while time.time() - start < int(scroll_time):
    print('正在滚动页面，倒计时：', int(scroll_time) - int(time.time() - start))
    img = web.eles('tag:img@src')
    web.scroll.down(500)
print('检测到图片数量：', len(img))
time.sleep(2)
print('开始下载图片')
for i in img:
    mission = web.download(i.attr('src'), 'img', 'img.png', show_msg=False)
    print('保存到：', mission[1])
web.close_driver()
