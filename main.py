from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Проверка наличия на странице элементов ui
def test_name_submit_form():
    driver = webdriver.Chrome('drv/chromedriver')
    driver.get('https://roustam.github.io/form.html')

    # checking links

    driver.find_element_by_link_text('Link 1')
    driver.find_element_by_link_text('Link 2')
    driver.find_element_by_link_text('Link 3')

    #checking inputs

    driver.find_element_by_id('input_text').click()

    driver.find_element_by_id('sec_input_text')
    driver.find_element_by_id('pat_input_text')

    # check labels
    driver.find_elements(By.TAG_NAME, 'label')

    #check buttons

    driver.find_elements_by_tag_name('button')
    driver.close()

full_str = '''Введите значение для поля Имя
Введите значение для поля Фамилия
Введите значение для поля Отчество
Укажите значение поля "возраст"
'''

short_srt = '''Введите значение для поля Фамилия
'''

# Проверка случаев, когда не заполнены все поля
def test_input_conditions():
    driver = webdriver.Chrome('drv/chromedriver')
    driver.get('https://roustam.github.io/form.html')

    first_name_input = driver.find_element_by_id('input_text')
    first_name_input.send_keys('Иван')
    last_name_input = driver.find_element_by_id("sec_input_text")
    last_name_input.send_keys('Иванов')
    pat_input = driver.find_element_by_id('pat_input_text')
    pat_input.send_keys('Иванович')
#    time.sleep(3)
    driver.find_element_by_id('reset').click()

#    textarea = driver.find_elements_by_tag_name('textarea')
    assert driver.find_element_by_id('bottomPanel').get_attribute("value") == "Содержимое удалено"

    driver.find_element_by_id('submit').click()

    print('--->', driver.find_element_by_id('bottomPanel').get_attribute("value"))
    assert driver.find_element_by_id('bottomPanel').get_attribute("value") == full_str
    age_selector = driver.find_element_by_tag_name('select')
    age_selector.click()
    age_selector.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.RETURN)

    pat_input.send_keys('Иванович')
    first_name_input.send_keys('Иван')
    driver.find_element_by_id('submit').click()

    assert driver.find_element_by_id('bottomPanel').get_attribute("value") == short_srt

    driver.close()