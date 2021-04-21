# import requests
#
# response = requests.get('https://www.engineerspock.com/')
# github_response = requests.get('https://api.github.com/')
#
# print(github_response.headers, end='\n')
# print(response)
import requests


def get_prices():
    coins = ["DOGE", "ETH", "DASH", "LTC"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":
    print(get_prices())
