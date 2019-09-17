import os
import logging
import logging.handlers
from conftest import BASE_DIR, now_time


# 日志管理
def init_logger():
    log_file_name = now_time + "log.txt"            # 使用当前时间当做log日志的文件名
    log_file = os.path.join(BASE_DIR, "logs/", log_file_name)
    dir_path = os.path.dirname(log_file)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except Exception:
        pass

    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=20 * 1024 * 1024, backupCount=10, encoding='utf-8')
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger_instance = logging.getLogger('logs')
    logger_instance.addHandler(handler)
    logger_instance.setLevel(logging.DEBUG)
    return logger_instance


def get_logger():
    logger = init_logger()
    return logger

# 日志配置
logger = get_logger()