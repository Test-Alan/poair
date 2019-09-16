import os
import sys
sys.path.append("os.path.dirname(os.path.abspath(__file__))")
from pages.xueqiu_page import LoginPage


class TestXueQiu:

    # 测试搜索
    def test_search(self, app):
        page = LoginPage(app)
        page.search("alibaba")
        assert page.get_text() == "BABA"