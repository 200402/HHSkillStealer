import requests
from  bs4 import BeautifulSoup as bs


def main():
    name = input("Введите ссылку на первую страницу: ") + "&page="
    a = 1+1

if __name__ == '__main__':
    main()



response = requests.get('https://ufa.hh.ru/search/vacancy', params=params, headers=headers)