import time
import random
import csv
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup


URL = "https://cbr.ru"


def extract_questions(dropdown_questions: Optional[List], rubric_title: str, theme_name: str = "") -> List[Dict]:
    items = []
    for dropdown_question in dropdown_questions:
        try:
            question = dropdown_question.find("h3") if dropdown_question.find("h3") else dropdown_question.find("h2")
            question = question.get_text().strip().replace("\xa0", " ")
            answer = dropdown_question.find("div", class_="additional-text-block").get_text().strip().replace("\xa0", " ")
            
            items.append({"title": rubric_title,"theme": theme_name, "question": question, "answer": answer})
        except Exception:
            print(f"Failed to parse question. Rubric: {rubric_title} \nTheme: {theme_name} \nDropdown_question: \n{dropdown_question}")

    return items


def get_data(url: str = URL):
    response = requests.get(url=url + "/faq/")
    soup = BeautifulSoup(response.text, "lxml")

    rubrics = soup.find_all(class_="rubric_title")

    data = []
    for rubric in rubrics:
        rubric_title = rubric.get_text().replace("\xa0", " ")
        rubric_url = url + rubric.get("href")
        print(rubric_title, rubric_url)

        res = requests.get(rubric_url)
        rubric_soup = BeautifulSoup(res.text, "lxml")
        categories = rubric_soup.find_all("div", class_="dropdown dropdown_container")

        if not categories:
            dropdown_questions = rubric_soup.find_all("div", class_="dropdown question")
            items = extract_questions(
                dropdown_questions=dropdown_questions, rubric_title=rubric_title
            )
            data.extend(items)
            continue

        for category in categories:
            theme = category.find("div", class_="dropdown_title referenceable")
            if theme:
                theme_name = theme.find("h2").get_text().replace("\xa0", " ")
                dropdown_questions = category.find_all("div", class_="dropdown question")
                items = extract_questions(
                    dropdown_questions=dropdown_questions, rubric_title=rubric_title, theme_name=theme_name
                )
                data.extend(items)
            else:
                time.sleep(random.randint(1, 2))

                theme = category.find("div", class_="dropdown_title-link").find("a", class_="dropdown_link referenceable")
                theme_url = url + theme.get("href")
                theme_name = theme.get_text().replace("\xa0", " ")

                theme_response = requests.get(theme_url)
                theme_soup = BeautifulSoup(theme_response.text, "lxml")

                dropdown_questions = theme_soup.find_all("div", class_="dropdown question")
                items = extract_questions(
                    dropdown_questions=dropdown_questions, rubric_title=rubric_title, theme_name=theme_name
                )
                data.extend(items)
    
    return data


def write_data(data: List[Dict], csv_file_path: str = "data/questions.csv"):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["title", "theme", "question", "answer"])
        
        csv_writer.writeheader()
        csv_writer.writerows(data)

    print(f"Данные успешно сохранены в файл: {csv_file_path}")


def main():
    data = get_data()
    write_data(data)


if __name__ == "__main__":
    main()
