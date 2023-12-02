import requests
import re

def get_subheadings(url):
    # Отправляем GET-запрос по указанному URL и получаем содержимое страницы
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        subheading_pattern = re.compile(r'<h3.*?>(.*?)<\/h3>', re.DOTALL)
        subheadings = re.findall(subheading_pattern, response.text)
        
        return subheadings
    else:
        print(f"Ошибка {response.status_code}: Невозможно получить доступ к странице.")

url = "http://www.columbia.edu/~fdc/sample.html"
result = get_subheadings(url)
print(result) 