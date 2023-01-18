import requests
import config
import time
from collections import Counter as cou
from bs4 import BeautifulSoup as bs


def main():
    link = input("Введите ссылку: ")
    allVacancyInOnePage = GetAllVacancyInOnePage(link)
    counter = 0
    allSkils = []
    while len(allVacancyInOnePage) > 0:
        counter += 1
        for vacancyLink in allVacancyInOnePage:
            skills = GetAllSkillsPerOneVacancy(vacancyLink.get("href"))
            for skill in skills:
                allSkils.append(skill.text)
            time.sleep(0.5)
        time.sleep(0.5)
        print("---------------------------")
        allVacancyInOnePage = GetAllVacancyInOnePage(link + f"&page={counter}")
    raritySkills = cou(allSkils)
    f = open('text.txt', 'w', encoding='utf-8')
    for raritySkill in raritySkills:
        f.write(raritySkill + ": " + str(raritySkills[raritySkill]) + '\n')



def GetAllVacancyInOnePage(link):
    return bs(requests.get(link, headers=config.headers).text, "lxml").find_all("a", class_="serp-item__title")


def GetAllSkillsPerOneVacancy(link):
    return bs(requests.get(link, headers=config.headers).text, "lxml").find_all("span", class_="bloko-tag__section bloko-tag__section_text")


if __name__ == '__main__':
    main()
