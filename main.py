from bs4 import BeautifulSoup
from urllib.request import urlopen


last_page_index = 2
BASE_URL = "http://ask.carnoc.com"


def gen_urls():
    # 帖子列表url
    for page in range(1, last_page_index):
        url = f"{BASE_URL}/typelist.jsp?wdtype=0&flag=2&type=0&page={page}"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")
        title_urls = soup.find_all(class_="title")
        with open("db.txt", "a+") as f:

            for title_url in title_urls:
                ask_title = title_url.text

                ask_detail_url = f"{BASE_URL}" + title_url.attrs.get("href")
                html = urlopen(ask_detail_url).read()
                soup = BeautifulSoup(html, "lxml")
                # # 问题描述 #question_content > cd > pre
                # question_content = soup.select("#question_content > cd > pre")[
                #     0
                # ].text
                f.write(ask_title + "\n")

                # 最佳答案 #best_answer_content > ca > pre
                best_answer_content = soup.select(
                    "#best_answer_content > ca > pre"
                )[0].text.strip()
                f.write(best_answer_content + "\n")


if __name__ == "__main__":
    gen_urls()
