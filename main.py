import requests
import config
import time
from bs4 import BeautifulSoup as bs


def main():
    link = input("Введите ссылку: ")
    var = getAllVacancyInOnePage(link)
    counter = 0
    while len(var) > 0:
        counter += 1
        for item in var:
            print(item.text)
        time.sleep(3)
        print("---------------------------")
        var = getAllVacancyInOnePage(link + f"&page={counter}")


def getAllVacancyInOnePage(link):
    return bs(requests.get(link, headers=config.headers).text, "lxml").find_all("a", class_="serp-item__title")


if __name__ == '__main__':
    main()
