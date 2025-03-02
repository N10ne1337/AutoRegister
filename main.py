from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Функция для генерации случайных данных
def generate_random_name():
    first_names = ["James", "John", "Robert", "Michael", "William"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    return random.choice(first_names), random.choice(last_names)

def generate_random_company():
    companies = ["TechCorp", "InnovateInc", "GlobalSolutions", "FutureTech", "NextGen"]
    return random.choice(companies)

def generate_random_employees():
    return random.randint(1, 1000)

def generate_random_phone():
    return f"+1{random.randint(200, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"

# Запрос email и кода авторизации у пользователя
email = input("Введите ваш email: ")
auth_code = input("Введите код авторизации: ")

# Настройка WebDriver в headless-режиме
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск без графического интерфейса
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://app.langdock.com/login")

try:
    # Ввод email
    email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")  # Поиск поля email по типу
    email_field.send_keys(email)
    time.sleep(1)

    # Поиск и нажатие кнопки "Зарегистрировать/Войти"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))  # Поиск кнопки по типу
    )
    login_button.click()
    time.sleep(2)

    # Ввод кода авторизации
    code_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))  # Поиск поля кода по типу
    )
    code_field.send_keys(auth_code)
    code_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # Генерация и ввод случайных данных
    first_name, last_name = generate_random_name()
    company_name = generate_random_company()
    employees = generate_random_employees()
    phone = generate_random_phone()

    # Заполнение полей
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys(first_name)  # Поиск по placeholder
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Company']").send_keys(company_name)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Employees']").send_keys(str(employees))
    driver.find_element(By.CSS_SELECTOR, "select[name='country']").send_keys("USA")  # Поиск выпадающего списка
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Phone']").send_keys(phone)

    # Нажатие кнопки регистрации
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Поиск кнопки по типу
    time.sleep(5)

    # Переход в настройки для получения API
    driver.find_element(By.CSS_SELECTOR, "a[href*='settings']").click()  # Поиск ссылки на настройки
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href*='api']").click()  # Поиск ссылки на API
    time.sleep(2)

    # Получение API ключа
    api_key = driver.find_element(By.CSS_SELECTOR, "code").text  # Поиск API ключа в теге <code>
    print(f"Ваш API ключ: {api_key}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()д
