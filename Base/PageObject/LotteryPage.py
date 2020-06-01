# -*- coding:utf-8 -*-
# @Time : 2020/5/25 17:12
# @Author : Administrator
# @File : LotteryPage.py
# @Software: PyCharm
# @Motto: good good study,day day up

from Base.BasePage import BasePage
from loguru import logger
from selenium.webdriver.common.by import By
from config.conf import LOTTERY_URL


class LotteryPage(BasePage):
    """封装彩票大厅相关操作步骤"""

    # 选择日期
    loc1 = (By.XPATH, "//div[@id='select_date']")
    # 选择某一天
    loc2 = (By.XPATH, "/td[contains(text(),'25')]")
    # 日期选择框的确定
    loc3 = (By.XPATH, "//a[@id='laydate_ok']")
    # 查询按钮
    loc4 = (By.XPATH, "//div[@id='dayBtn']//span[@class='font']")
    # 历史开奖区域
    loc5 = (By.XPATH, "//div[@class='lotteryPublic_contentBlock']")
    #
    loc6 = (By.XPATH, "//tr[44]//td[1]")
    # 日期框定位
    loc7 = (By.XPATH, "//div[@id='select_date']")
    # 模块标题
    loc8 = (By.XPATH, "//span[@class='lp_tb_title']")
    # 开奖视频
    loc9 = (By.XPATH, "//li[1]//div[1]//div[1]//ul[1]//li[2]//a[1]")
    # 今日号码
    loc10 = (By.XPATH, "//li[1]//div[1]//div[1]//ul[1]//li[3]//a[1]")
    # 冷热分析
    loc11 = (By.XPATH, " //li[1]//div[1]//div[1]//ul[1]//li[4]//a[1]")
    # 特码分析
    loc12 = (By.XPATH, " //li[1]//div[1]//div[1]//ul[1]//li[5]//a[1]")
    # 投资价值
    loc13 = (By.XPATH, "//li[1]//div[1]//div[1]//ul[1]//li[6]//a[1]")
    # 号码规律
    loc14 = (By.XPATH, "//div[@class='public_main']//li[7]//a[1]")
    # 開號統計
    loc15 = (By.XPATH, "//div[@class='public_main']//li[8]//a[1]")
    # 更多
    loc16 = (By.XPATH, " //span[@class='more active']")
    # 冠亞和遺漏
    loc17 = (By.XPATH, " //div[@class='public_main']//li[9]//a[1]")
    # 號碼遺漏
    loc18 = (By.XPATH, "//div[@class='public_main']//li[10]//a[1]")
    # 历史统计
    loc19 = (By.XPATH, "//div[@class='public_main']//li[11]//a[1]")
    # 每日長龍
    loc20 = (By.XPATH, "//div[@class='public_main']//li[12]//a[1]")
    # 遺漏大數據
    loc21 = (By.XPATH, "//body//li[13]")
    # 特殊形態統計
    loc22 = (By.XPATH, "//body//li[14]")
    # 號碼走位報警
    loc23 = (By.XPATH, "//body//li[15]")
    # 兩面數據統計
    loc24 = (By.XPATH, "//body//li[16]")
    # 綜合路珠
    loc25 = (By.XPATH, "//div[@class='public_main']//li[2]//div[1]//div[1]//ul[1]//li[1]//a[1]")
    # 单双大小路珠
    loc26 = (By.XPATH, "//div[@class='public_main']//li[2]//div[1]//div[1]//ul[1]//li[2]//a[1]")
    # 龙虎路珠
    loc27 = (By.XPATH, "//div[@class='public_main']//li[2]//div[1]//div[1]//ul[1]//li[3]//a[1]")
    # 冠亞和路珠
    loc28 = (By.XPATH, "//div[@class='public_main']//li[2]//div[1]//div[1]//ul[1]//li[4]//a[1]")
    # 號碼前後路珠
    loc29 = (By.XPATH, "//div[@class='public_main']//li[2]//div[1]//div[1]//ul[1]//li[5]//a[1]")
    # 單雙大小走勢圖
    loc30 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[1]//a[1]")
    # 橫版走勢圖
    loc31 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[2]//a[1]")
    # 位置走勢
    loc32 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[3]//a[1]")
    # 號碼走勢
    loc33 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[4]//a[1]")
    # 冠亞和走勢
    loc34 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[5]//a[1]")
    # 自選走勢
    loc35 = (By.XPATH, "//li[3]//div[1]//div[1]//ul[1]//li[6]//a[1]")
    # 免费参考
    loc36 = (By.XPATH, "//div[@class='funBlock last']//li[1]//a[1]")
    # 公式參考
    loc37 = (By.XPATH, "//div[@class='funBlock last']//li[2]//a[1]")
    # 闖關計劃
    loc38 = (By.XPATH, "//div[@class='funBlock last']//li[3]//a[1]")
    # 殺號定膽
    loc39 = (By.XPATH, "//div[@class='funBlock last']//li[4]//a[1]")
    # 推薦計劃
    loc40 = (By.XPATH, "//div[@class='funBlock last']//li[5]//a[1]")
    # 九宮計劃
    loc41 = (By.XPATH, "//div[@class='funBlock last']//li[6]//a[1]")

    def open_url(self):
        self.load_url(LOTTERY_URL)

    def click_kaijiang(self):
        self.open_url()
        self.sleep(3)
        # self.click(*self.loc1)
        # self.click(*self.loc2)
        # self.click(*self.loc4)
        # js = 'document.getElementById("select_date").removeAttribute("readonly");'
        # self.run_script_1(js)
        text = self.get_element_text(*self.loc8)
        return text

    def click_shipin(self):
        self.open_url()
        self.click(*self.loc9)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_opencodeanalysis(self):
        self.open_url()
        self.click(*self.loc10)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_coldhotnumber(self):
        self.open_url()
        self.click(*self.loc11)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_specialview(self):
        self.open_url()
        self.click(*self.loc12)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_investmentvalue(self):
        self.open_url()
        self.click(*self.loc13)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_numberrulestat(self):
        self.open_url()
        self.click(*self.loc14)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_kaihaoview(self):
        self.open_url()
        self.click(*self.loc15)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_gyhomit(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc17)
        text = self.get_element_text(*self.loc8)
        return text

    def click_yilou(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc18)
        text = self.get_element_text(*self.loc8)
        return text

    def click_ballstat(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc19)
        text = self.get_element_text(*self.loc8)
        return text

    def click_changlongdaystat(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc20)
        text = self.get_element_text(*self.loc8)
        return text

    def click_omitdata(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc21)
        text = self.get_element_text(*self.loc8)
        return text

    def click_specialformdata(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc22)
        text = self.get_element_text(*self.loc8)
        return text

    def click_numpositionalarm(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc23)
        text = self.get_element_text(*self.loc8)
        return text

    def click_twosidedstat(self):
        self.open_url()
        self.sleep(5)
        self.action_chains(*self.loc16)
        self.click(*self.loc24)
        text = self.get_element_text(*self.loc8)
        return text

    def clcik_luzhuanalysis(self):
        self.open_url()
        self.click(*self.loc25)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_luzhubigorsmall(self):
        self.open_url()
        self.click(*self.loc26)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_luzhulonghu(self):
        self.open_url()
        self.click(*self.loc27)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_guanyahestat(self):
        self.open_url()
        self.click(*self.loc28)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_luzhuleftorright(self):
        self.open_url()
        self.click(*self.loc29)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_bsoetrend(self):
        self.open_url()
        self.click(*self.loc30)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_zoushitu(self):
        self.open_url()
        self.click(*self.loc31)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_positiontrend(self):
        self.open_url()
        self.click(*self.loc32)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_numbertrend(self):
        self.open_url()
        self.click(*self.loc33)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_guanyatrend(self):
        self.open_url()
        self.click(*self.loc34)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_positionanalyze(self):
        self.open_url()
        self.click(*self.loc35)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_betgame(self):
        self.open_url()
        self.click(*self.loc36)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_formula(self):
        self.open_url()
        self.click(*self.loc37)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_passplan(self):
        self.open_url()
        self.click(*self.loc38)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_shdd(self):
        self.open_url()
        self.click(*self.loc39)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_shdd(self):
        self.open_url()
        self.click(*self.loc39)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_numberplan(self):
        self.open_url()
        self.click(*self.loc40)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text

    def click_nineplan(self):
        self.open_url()
        self.click(*self.loc41)
        self.sleep(3)
        text = self.get_element_text(*self.loc8)
        return text


if __name__ == '__main__':
    pass
