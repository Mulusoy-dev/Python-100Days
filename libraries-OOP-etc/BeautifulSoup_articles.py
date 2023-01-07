from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
#print(soup.title)

# headings = soup.select("tr", class_="athing")
#
# for tag in headings:
#     print(tag.text)


articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.find("a").get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


#print(article_texts)
#print(article_links)
print(article_upvotes)


max_item = max(article_upvotes)
max_item_index = article_upvotes.index(max_item)
print(max_item)
print(max_item_index)

print(f' {article_texts[28]}, {article_links[28]}, {max_item}')








# import lxml
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.title)                                            # Title Information
# print(soup.title.string)                                     # Web Title Name Information
# print(soup.prettify())                                       # HTML appearance
# print(soup.a)                                                # First Web Link Information (a tag)
# print(soup.p)                                                # First Paragraph Information (p tag)

####################################################################################################################
# all_anchor_tags = soup.find_all(name="a")                    # All Web Link Information (all a tag)
# print(all_anchor_tags)

# for tag in all_anchor_tags:                                  # getText() is using to access 'text' strings
#     print(tag.getText())
#     print(tag.get("href"))                                   # get() is using to access 'link' strings

# all_paragraphs_tags = soup.find_all(name="p")                # All Paragraph Information (all p tag)
# print(all_paragraphs_tags)
#####################################################################################################################


# headings = soup.find(name="h1", id="name")                    # 2.solution (attribute access)
# print(headings)

# urls = soup.select_one(selector="p a")                        # p,a tag access (CSS Selector)
# print(urls)

# headings = soup.select("td", class_="title")                    # class attribute access
