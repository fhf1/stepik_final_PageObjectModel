from selenium.common.exceptions import NoSuchElementException

# Сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# Здесь опишем вспомогательные методы для работы с драйвером.

class BasePage():
    # Добавим конструктор — метод, который вызывается, когда мы создаем объект. 
    # Конструктор объявляется ключевым словом __init__
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True