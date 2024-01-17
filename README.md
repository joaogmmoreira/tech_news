# Web Scraper Study Project

This project is a simple web scraper built for study purposes. It's written in Python and uses the `requests` and `Scrapy` libraries to fetch and parse HTML content.

## Overview

The project consists of a Python script, `scraper.py`, which contains several functions each performing a specific task in the web scraping process.
The `search_engine.py` script extends the functionality of the web scraper by providing several search features. These features allow you to search the scraped data based on different criteria.

### Functions

-   `scrape_updates(html_content)`: This function takes HTML content as input and returns all the links contained within `<a>` tags with the class `cs-overlay-link`.

-   `scrape_next_page_link(html_content)`: This function takes HTML content as input and returns the link contained within the `<a>` tag with the class `next`.

-   `scrape_news(html_content)`: This function takes HTML content as input and extracts various pieces of information from specific elements. The extracted information includes the URL, title, timestamp, writer, reading time, summary, and category of a news article.

-   `search_by_title(title)`: This function allows you to search the scraped news articles by their title. It takes a title as an argument and returns a list of tuples. Each tuple contains the title and URL of a news article that matches the search term.

-   `search_by_date(date)`: This function allows you to search the scraped news articles by their publication date. It takes a date in the format "YYYY-MM-DD" as an argument and returns a list of tuples. Each tuple contains the title and URL of a news article that was published on the given date. If the date is not in the correct format, the function raises a ValueError with the message "Data inválida".

-   `search_by_category(category)`: This function is a placeholder for a feature that will allow you to search the scraped news articles by their category. This function is not yet implemented.

## Usage

To use this script, you need to have Python and the `requests` and `Scrapy` libraries installed. You can then run the script from the command line, passing the URL of the webpage you want to scrape as an argument.

Please note that this project is for study purposes only. Always respect the terms of service of the website you are scraping and do not use this script for any illegal activities.

## Future Work

This is a basic web scraper and there's a lot of room for improvement. Future updates could include handling pagination, adding error handling, or expanding the types of data the script can extract.
