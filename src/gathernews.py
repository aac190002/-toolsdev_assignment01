"""
Asmita Chitale
Assignment 01
ATCM 3311.0U1
06/11/2020
"""

import nltk
import newspaper

SOURCES = [
    u"https://arstechnica.com/",
    u"https://www.mentalfloss.com/",
    u"https://www.wired.com/"
]

def user_keyword ():
    """
    Ask user for a keyword
    :return: the keyword
    """
    userinput = input("Please enter any keyword (press enter to continue): ")
    return userinput

def get_articles():
    """
    Gets all of the latest articles from SOURCES
    :return: List of Articles
    """
    newspapers = [newspaper.build(url, memoize_articles=False) for url in SOURCES]
    articles = [][:]
    for paper in newspapers:
        articles.extend(paper.articles)
    return articles

if __name__ == '__main__':
    # Ask user for keyword input
    keyword = user_keyword()

    # Get articles
    articles = get_articles()

    # Filter by keyword

    # Extra feature

    pass