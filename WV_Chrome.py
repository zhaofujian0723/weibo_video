# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import requests
from tkinter import *


class WeiBoVideo(object):

    def __init__(self):
        pass

    def start(self, url):
        driver = webdriver.Chrome(".\chromedriver.exe")
        driver.get(url)

        time.sleep(5)

        v_link = driver.find_element_by_xpath('//div[@class="weibo_player_fa"]/div[@node-type="common_video_player"]/div/div/video' ).get_attribute("src")
        name = driver.find_element_by_xpath('//div[@class="info_txt W_f14"]').text

        driver.close()

        response = requests.get(v_link)

        if response.status_code == 200:
            content = response.content
            with open("{}.mp4".format(name), "wb") as f:
                f.write(content)
        else:
            print("下载失败")


def on_click():
    kw = xls_text.get()  # 获取外部输入爬取链接
    weibo = WeiBoVideo()
    weibo.start(kw)


if __name__ == '__main__':
    # link = input("请输入需要下载的视屏地址:")
    # start(link)
    """使用tkinter构建参数获取输入框"""
    root = Tk()  # 构建表单对象
    root.title("微博视频下载")  # 表格标题
    root.geometry('300x300')  # 表单尺寸 是x 不是 *

    l1 = Label(root, text="请输入视屏地址:")  # 创建一个表单标签
    l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    xls_text = StringVar()  # 接收参数类型
    xls = Entry(root, textvariable=xls_text)
    xls_text.set(" ")
    xls.pack()

    Button(root, text="确认", command=on_click).pack()

    root.mainloop()
