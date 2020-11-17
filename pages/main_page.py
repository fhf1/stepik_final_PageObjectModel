# Реализуем Page Object, который будет связан с главной страницей интернет-магазина

# Импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By

# Класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
class MainPage(BasePage):
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage,
        # обращаться к нему нужно соответствующим образом с помощью self
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        