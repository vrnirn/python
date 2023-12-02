import requests
import json

def get_millennium_falcon_info():
    # Получаем информацию о корабле Millennium Falcon
    url = "https://swapi.dev/api/starships/?search=Millennium Falcon"
    response = requests.get(url)
    data = response.json()

    # Получаем детали о Millennium Falcon
    if data['count'] > 0:
        millennium_falcon = data['results'][0]
        return millennium_falcon
    else:
        return None

def get_planet_info(planet_url):
    # Получаем информацию о планете
    response = requests.get(planet_url)
    planet_data = response.json()

    # Формируем информацию о планете
    planet_info = {
        'name': planet_data['name']
    }

    return planet_info

def get_pilot_info(pilot_url):
    # Получаем информацию о пилоте
    response = requests.get(pilot_url)
    pilot_data = response.json()

    # Получаем информацию о родной планете пилота
    homeworld_url = pilot_data['homeworld']
    homeworld_info = get_planet_info(homeworld_url)

    # Формируем информацию о пилоте
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld': homeworld_info['name'],
        'homeworld_url': homeworld_url
    }

    return pilot_info

def main():
    # Получаем информацию о Millennium Falcon
    millennium_falcon_info = get_millennium_falcon_info()

    if millennium_falcon_info:
        # Формируем информацию о пилотах
        pilots_info = []
        for pilot_url in millennium_falcon_info['pilots']:
            pilot_info = get_pilot_info(pilot_url)
            pilots_info.append(pilot_info)

        # Формируем общую информацию о Millennium Falcon
        millennium_falcon_data = {
            'name': millennium_falcon_info['name'],
            'max_speed': millennium_falcon_info['max_atmosphering_speed'],
            'class': millennium_falcon_info['starship_class'],
            'pilots': pilots_info
        }

        # Выводим информацию на экран
        print(json.dumps(millennium_falcon_data, indent=2))

        # Сохраняем информацию в JSON-файл
        with open('millennium_falcon_info.json', 'w') as json_file:
            json.dump(millennium_falcon_data, json_file, indent=2)

if __name__ == "__main__":
    main()