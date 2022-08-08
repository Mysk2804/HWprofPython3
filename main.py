import csv
import requests
import bs4


def nabr_parser(keywords):
    # result = []
    HEADERS = {'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Cookie': '_ga=GA1.2.1306413108.1652587777; _ym_uid=1652587777523461067; _ym_d=1652587777; fl=ru; hl=ru; visited_articles=140734; habr_web_home_feed=/all/; _ym_isad=1; _gid=GA1.2.1840323510.1659927436',
               'Host': 'habr.com',
               'Referer':'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
               'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
               'sec-ch-ua-mobile': '?0',
               'sec-ch-ua-platform': '"Windows"',
               'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-Fetch-User': '?1',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
    response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    text = response.text
    # print(text)

    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('div', class_='tm-article-snippet')
    # print(len(articles))

    for article in articles:
        hubs = article.find_all(class_='tm-article-snippet__hubs')
        hubs = {hub.find('a').text.strip(' *').lower() for hub in hubs}
        # print(hubs)
        if hubs & keywords:
            article_teg_a = article.find('h2').find('a')
            articles_teg_div = article.find(class_='tm-article-snippet__datetime-published').find('time')
            times = articles_teg_div.attrs['title']
            href = article_teg_a.attrs['href']
            url = 'https://habr.com' + href
            # resul = [times, article_teg_a.text, url]
            # result.append(resul)
            # return result
            print(f'{times} -- {article_teg_a.text} -- {url}')

# def save_result(result):
#     header = ('Время',
#               'Название',
#               'Ссылка')
#     with open('result.csv', 'w', encoding='utf-8') as f:
#         writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(header)
#         for item in result:
#             writer.writerow(item)


if __name__ == '__main__':
    KEYWORDS = {'дизайн', 'сетевые технологии', 'управление сообществом', 'python'}
    nabr_parser(KEYWORDS)
    # save_result(nabr_parser(KEYWORDS))
