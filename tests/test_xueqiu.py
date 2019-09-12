from pages.xueqiu_page import LoginPage


class TestXueQiu:

    # 测试搜索
    def test_search(self, endevice):
        page = LoginPage(endevice)
        page.search("alibaba")
        assert page.get_text() == "BABA"