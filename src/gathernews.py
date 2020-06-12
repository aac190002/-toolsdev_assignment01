"""
Asmita Chitale
Assignment 01
ATCM 3311.0U1
06/11/2020
"""

# IMPORTS
import nltk
import newspaper
import os
import progressbar
import sys
import webbrowser

# CONSTS
SOURCES = [
    u"https://arstechnica.com/",
    u"https://www.mentalfloss.com/",
    u"https://www.wired.com/"
]
OUTFILE = "../news_summary.txt"
PAGE_TEMPLATE = "page_template.html"
CARD_TEMPLATE = "card_template.html"
OUTHTML = "../yournews.html"

# SETUP
nltk.download('punkt')


def user_keyword ():
    """
    Ask user for a keyword
    :return: the keyword
    """
    print("Please enter any keyword (press enter to continue): ", end='', file=sys.stderr)
    userinput = input("")
    return userinput


def get_articles():
    """
    Gets all of the latest articles from SOURCES
    :return: List of Articles
    """
    newspapers = [newspaper.build(url, memoize_articles=False) for url in SOURCES]
    articles = [][:]
    for i, paper in enumerate(newspapers):
        print("Scraping " + SOURCES[i] + " ...", end='', file=sys.stderr)
        articles.extend(paper.articles)
        print(" %d found." % len(paper.articles), file=sys.stderr)
    print("Found %d articles." % len(articles), file=sys.stderr)
    return articles


def process_articles(articles):
    """
    Download, parse, and NLP articles
    :param articles: List of Articles
    :return: Processed list of Articles
    """
    print("Processing articles ...", file=sys.stderr)
    good_articles = [][:]
    failures = 0
    for article in progressbar.progressbar(articles):
        try:
            article.download()
            article.parse()
            article.nlp()
            good_articles.append(article)
        except newspaper.ArticleException:
            failures += 1
    print("%d of %d articles failed to process." % (failures, len(articles)), file=sys.stderr)
    return good_articles


def filter_articles(articles, keyword):
    """
    Filters articles by keyword
    :param articles: List of processed Articles
    :param keyword: Filtering keyword
    :return: Filtered, processed list of Articles
    """
    print("Filtering ...", file=sys.stderr)

    def filter_function(article):
        keywords = [word.lower() for word in article.keywords]
        keyword_lower = keyword.lower()
        return keyword_lower in keywords

    good_articles = list(filter(filter_function, articles))
    print("%d articles match filter." % len(good_articles), file=sys.stderr)

    return good_articles


def save_articles(articles):
    """
    Save the filtered articles to OUTFILE
    :param articles: Filtered, processed list of Articles
    :return: None
    """
    print("Saving article summaries.", file=sys.stderr)
    with open(OUTFILE, "w") as outfile:
        for article in articles:
            outfile.write(article.title)
            outfile.write(" - ")

            # Comma separated author list
            first_author = True
            for author in article.authors:
                if first_author:
                    first_author = False
                else:
                    outfile.write(", ")
                outfile.write(author)

            outfile.write("\n")
            outfile.write(article.summary)
            outfile.write("\n")
            outfile.write("\n")


def html_page(articles, keyword):
    """
    Extra feature: Make an HTML summary page of the articles with pictures and links using Bootstrap
    Uses the top_image feature in newspaper3k

    https://getbootstrap.com/

    :param articles: Filtered, processed list of Articles
    :param keyword: the keyword
    :return: None
    """
    # Internal function to fix non-ASCII characters:
    def fix_ascii(text):
        return text.encode('ascii', 'xmlcharrefreplace').decode("utf-8")

    print("Generating custom HTML page.", file=sys.stderr)

    with open(CARD_TEMPLATE, "r") as cardfile:
        card_template = cardfile.read()
    with open(PAGE_TEMPLATE, "r") as pagefile:
        page_template = pagefile.read()

    # Make a card for each article
    card_content = ""
    for article in articles:
        # Need to escape unicode characters
        tmp_card = card_template.format(image=article.top_image,
                                        title=fix_ascii(article.title),
                                        link=article.url)
        card_content += tmp_card

    # Save page
    if keyword:
        keyword_text = " - " + keyword
    else:
        keyword_text = ""
    # Need to escape unicode characters
    page_content = page_template.format(keyword=fix_ascii(keyword_text),
                                        keyword2=fix_ascii(keyword_text),
                                        content=card_content)
    with open(OUTHTML, "w") as outhtml:
        outhtml.write(page_content)

    # Open page
    html_path = os.path.abspath(OUTHTML)
    webbrowser.open_new_tab(html_path)


if __name__ == '__main__':
    # Ask user for keyword input
    keyword = user_keyword()

    # Get articles
    articles = get_articles()

    # Process articles
    articles = process_articles(articles)

    # Filter by keyword
    if keyword:
        articles = filter_articles(articles, keyword)

    # Save article summaries
    save_articles(articles)

    # Extra feature - Make HTML sumnmary page with links
    html_page(articles, keyword)

    print("Done.", file=sys.stderr)

    pass
