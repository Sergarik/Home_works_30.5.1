import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_pass




""" В написанном тесте (проверка карточек питомцев) c
  применением неявных ожиданий всех элементов (фото, имя питомца, его возраст). """
@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()


def test_implicitly_wait_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_pass)
    # неявное ожидание
    driver.implicitly_wait(7)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем что главная страница со всеми питомцами открыта верно
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # неЯвное ожидание
    driver.implicitly_wait(7)
    # Переходим в раздел Мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем питомцев в разделе Мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').text == 'Мои питомцы'

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    # Проверяем корректность данных питомцев
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

