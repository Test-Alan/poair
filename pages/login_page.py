from pages.base_page import BasePage


class LoginPage(BasePage):
    tv_search = "com.xueqiu.android:id/tv_search"
    search_input_text = "com.xueqiu.android:id/search_input_text"
    name = "阿里巴巴"
    stockCode = "BABA"

    def search(self, value):
        self.poco(self.tv_search).click()
        self.send_keys(value)
        self.poco(text=self.name).click()


    def get_text(self):
        return self.poco(text=self.stockCode).get_text()
