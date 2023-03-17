import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )

        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    content = selector.css("a.cs-overlay-link::attr(href)")

    return content.getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_button = selector.css("a.next::attr(href)")

    return next_page_button.get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a.url::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary = selector.css(
        "div.entry-content > p:first-of-type *::text"
        ).getall()
    category = selector.css("a.category-style > span.label::text").get()

    title = title.strip()
    reading_time = int(reading_time.split(" ")[0])
    summary = "".join(summary).strip()

    list = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }
    return list


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    list = []

    while len(list) < amount:
        response = fetch(url)
        update_news = scrape_updates(response)
        next_button = scrape_next_page_link(response)

        for update in update_news:
            response2 = fetch(update)
            news = scrape_news(response2)
            list.append(news)

        url = next_button

    create_news(list[:amount])
    return list[:amount]
