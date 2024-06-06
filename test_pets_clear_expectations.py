import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_pass


""" Проверка таблицы всех питомцев в разделе "Мои питомцы",
с добавлением явного ожидания элементов страницы  """
@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()

def test_show_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_pass)
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем что главная страница пользователя со всеми питомцами открыта верно
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
    # Переходим в раздел Мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем таблицу всех питомцев в разделе Мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').text == 'Мои питомцы'
    # Делаем скриншот
    driver.save_screenshot('my_pets.png')



def test_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_pass)
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем вход в аккаунт на главную страницу
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Делаем скриншот
    driver.save_screenshot('all_pets.png')

