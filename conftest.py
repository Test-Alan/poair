import os
import time
import pytest
from airtest.core.api import *


# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")


############################
# 连接哪个设备（Android/IOS）
server_prot = "Android://127.0.0.1:5037/"
# 手机设备(真机/模拟器)
device = server_prot + "127.0.0.1:7555?cap_method=JAVACAP&&ori_method=ADBORI"

# 失败重跑次数
rerun = "3"

# 运行测试用例的目录或文件
cases_path = "./tests/"

# 当前时间
now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

############################

def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2019_08_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


# 启动app
@pytest.fixture(scope='session', autouse=True)
def app():
    dev = connect_device(device)
    # script content
    print("start...")
    start_app("com.xueqiu.android")
    return dev

# 关闭app
@pytest.fixture(scope="session", autouse=True)
def app_shut():
    yield
    stop_app("com.xueqiu.android")
    time.sleep(2)
    print("test end!")



