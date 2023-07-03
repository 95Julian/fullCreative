import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Pages.basepage import Basepage


class Canvas(Basepage):
    ser = Service("D:/Julian/Softwares/chromedriver/chromedriver_win32/chromedriver")
    driver = webdriver.Chrome(service=ser)
    driver.get("http://www.htmlcanvasstudio.com/")
    print(driver.title)
    line = (By.CSS_SELECTOR, ".button.line")
    rectangle = (By.CSS_SELECTOR, ".button.rectangle")
    circle = (By.CSS_SELECTOR, ".button.ellipse")

    driver.maximize_window()
    canvas = (By.CSS_SELECTOR, "#container")
    eraser = (By.CSS_SELECTOR, ".button.eraser")
    action = ActionChains(driver)

    def __int__(self, driver):
        super().__init__(driver)

    # ******  Draw a Line ******
    def drawline(self):
        # Note : y axis (- co-ordinate goes up , + co-ordinate goes down) ; x axis (- co-ordinate goes left,
        # + co-ordinate goes right)
        self.do_click(self.line)
        time.sleep(2)
        canvas = self.driver.find_element(By.CSS_SELECTOR, "#container")
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(canvas, 0, 0).click_and_hold(canvas).move_by_offset(-200,
                                                                                               0).click().move_by_offset(
            100, -100).click().move_by_offset(0, 200).click().release().perform()
        time.sleep(3)

    # # ****** Draw a Rectangle *****
    def drawrectangle(self):
        self.do_click(self.rectangle)
        time.sleep(2)
        canvas = self.driver.find_element(By.CSS_SELECTOR, "#container")
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(canvas, -50, 150).click().move_by_offset(170, 80).click().perform()
        time.sleep(2)

    #
    # ****** click “use eraser” and erase the horizontal line *****
    def eraseline(self):
        self.do_click(self.eraser)
        time.sleep(1)
        canvas = self.driver.find_element(By.CSS_SELECTOR, "#container")
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(canvas, 0, 0).drag_and_drop_by_offset(canvas, -200,
                                                                                 0).release().perform()
        time.sleep(1)

    # ******  Draw a circle  *****
    def drawcircle(self):
        self.do_click(self.circle)
        time.sleep(2)
        canvas = self.driver.find_element(By.CSS_SELECTOR, "#container")
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(canvas, 140, -150).click().move_by_offset(30, 30).click().perform()
        time.sleep(3)

    #  ******  Erase the circle alone  *****
    def erasecircle(self):
        size = self.driver.find_element(By.ID, "slider")
        action = ActionChains(self.driver)
        canvas = self.driver.find_element(By.CSS_SELECTOR, "#container")
        action.move_to_element(size).drag_and_drop_by_offset(size, 90, 0).perform()
        time.sleep(1)
        self.do_click(self.eraser)
        time.sleep(2)
        i = 140
        while i < 320:
            self.action.move_to_element_with_offset(canvas, i, -120).drag_and_drop_by_offset(canvas, i,
                                                                                             -180).release().perform()
            i = i + 12
        time.sleep(2)
