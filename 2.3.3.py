from selenium import webdriver
import time
import math





try:
    link = "https://suninjuly.github.io/alert_accept.html?"
    browser = webdriver.Chrome()
    browser.get(link)
#давим кнопку
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    # Жмем ок
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

 #Cтроку в конце файла