from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    found_news = search_news(
            {"title": {"$regex": title, "$options": "i"}}
        )

    tuple_list = [
        (news["title"], news["url"]) for news in found_news
    ]

    return tuple_list


# Requisito 8
def search_by_date(date):
    try:
        new_date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        found_news = search_news(
            {"timestamp": new_date_format}
        )

        tuple_list = [
            (news["title"], news["url"]) for news in found_news
        ]

        return tuple_list

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
