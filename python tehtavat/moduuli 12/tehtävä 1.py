import requests


def ota_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('value')
    else:
        return "Failed to fetch Chuck Norris joke"


def main():
    vitsi = ota_chuck_norris_vitsi()
    print("Chuck Norris vitsi:")
    print(vitsi)


if __name__ == "__main__":
    main()
