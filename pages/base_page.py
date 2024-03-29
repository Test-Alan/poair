import allure
from airtest.core.api import *
from allure_commons.types import AttachmentType
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
from utils.logger import logger
from base64 import b64decode

class BasePage:

    def __init__(self, dev):
        self.poco = AndroidUiautomationPoco(dev, use_airtest_input=True, screenshot_each_action=False)
        # 黑名单元素，用来防止意外弹出处理
        self.black_list = ["aaa"]
        # 最大查找元素次数
        self.max = 2

    def poco_find(self, elm=None, **kwargs):
        try:
            logger.info("开始查找元素")
            if elm is not None:
                location = elm
            else:
                for k,v in kwargs.items():
                    location = k + "=" + v

            self.poco(elm, **kwargs).wait_for_appearance(timeout=10)
        except PocoTargetTimeout:
            if self.max <= 0:
                # 日志
                logger.info(format(self.__class__.__name__) + "页面" + "{}对象未找到".format(''.join(location)))
                allure.attach(self.poco_snapshot(), name=''.join(location) + "对象未找到截图.png",
                              attachment_type=AttachmentType.PNG)
                raise ("已到达最大查找次数，并未找到元素！")
            print("max=", self.max)
            self.max -= 1
            # bugs here as the panel not shown
            for black in self.black_list:
                element = self.poco(black).exists()
                if element:
                    self.poco(black).click()
                    logger.info("黑名单{}元素出现，已点击!".format(black))
                else:
                    logger.info("黑名单{}元素未出现!".format(black))

            else:
                return self.poco_find(elm, **kwargs)
        else:
            logger.info(format(self.__class__.__name__) + "页面" + "{}对象已找到".format(''.join(location)))
            return self.poco(elm, **kwargs)

    # 在设备屏幕上执行触摸操作
    def touch(self, v, times=1, **kwargs):
        touch(v, times, **kwargs)

    # 在设备屏幕上执行滑动操作。
    def swipe(self, v1, v2=None, vector=None, **kwargs):
        swipe(v1, v2, vector, **kwargs)

    # 在设备上执行键事件
    def keyevent(self, keyname, **kwargs):
        keyevent(keyname, **kwargs)

    # 等待
    def wait(self, v, timeout=None, interval=0.5, intervalfunc=None):
        wait(v, timeout, interval, intervalfunc)

    # 在目标设备上输入文本
    def send_keys(self, value, enter=True, **kwargs):
        text(value, enter, **kwargs)
    # airtest切图
    def snapshot(self, filename, msg):
        snapshot(filename, msg)

    # poco截图
    def poco_snapshot(self):

        b64img, fmt = self.poco.snapshot(width=720)
        return b64decode(b64img)



print(__name__)