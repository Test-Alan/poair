from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class BasePage:

    def __init__(self, dev):
        self.poco = AndroidUiautomationPoco(dev, use_airtest_input=True, screenshot_each_action=False)

    def poco(self, agent, **options):
        return self.poco(agent, **options)

    # 在设备屏幕上执行触摸操作
    def touch(self, v,times=1, **kwargs):
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


