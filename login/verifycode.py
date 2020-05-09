#!/usr/bin/env python
'''
@desc:    自定义图形验证码
@author:  
@contact: 
@file: verifycode.py
@time: 2020/3/3 11:03 上午
'''
import os
from io import BytesIO
from random import randint

from PIL import Image, ImageFont, ImageDraw


class VerifyCode:
    def __init__(self, width=100, height=40, size=4):
        """
        :param width: 验证码图片宽度
        :param height: 高度
        :param size: 字符数
        """
        self.width = width
        self.height = height
        self.size = size
        self.__code = ''  # 验证码字符串
        self.pen = None  # 画笔

    @property
    def code(self):
        return self.__code

    def generate(self):
        # 1)、创建画布
        im = Image.new("RGB",(self.width,self.height),self.__rand_color(150))
        self.pen = ImageDraw.Draw(im)
        # 2)、生成验证码字符串
        self.rand_string()
        # 3)、画验证码
        self.__draw_code()
        # 4)、画干扰点
        self.__draw_point()
        # 5)、画干扰线
        self.__rand_line()
        # 6)、返回验证码图片
        # 缓冲区
        buf = BytesIO()
        # 把图片放到缓冲区
        im.save(buf, 'png')
        # 获取图片的二进制
        res = buf.getvalue()
        buf.close()
        return res
        # im.save("vc.png")

    def __rand_color(self, min=0, max=255):
        return randint(min, max), randint(min, max), randint(min, max)

    # 验证码字符串
    def rand_string(self):
        self.__code = ''
        for i in range(self.size):
            self.__code += str(randint(0, 9))

    # 画验证码
    def __draw_code(self):
        # 加载字体
        path = os.path.join(os.getcwd(), 'static/fonts/SIMLI.TTF')
        print(path)
        font1 = ImageFont.truetype(path, size=20, encoding="utf-8")

        # 计算字符宽度
        width = (self.width-20) // self.size

        # 逐个字符画
        for i in range(len(self.__code)):
            x = 13 + width * i  # 计算每个字符的x坐标
            self.pen.text((x, 9), self.__code[i], font=font1, fill=self.__rand_color(0,80))

    # 画点
    def __draw_point(self):
        for i in range(100):
            self.pen.point((randint(1, self.width-1), randint(1, self.height-1)), self.__rand_color(30, 100))

    def __rand_line(self):
        for i in range(5):
            self.pen.line([(randint(1, self.width-1), randint(1, self.height-1)), (randint(1, self.width-1), randint(1, self.height-1))], fill=self.__rand_color(50,150), width=2)


# 单例属性
vc = VerifyCode()


if __name__ == '__main__':
    pass
