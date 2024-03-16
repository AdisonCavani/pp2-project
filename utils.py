from bs4 import BeautifulSoup
from requests import get
from classes import Review

def parseHtml(html: str) -> list[Review]:
    review_list: list[Review] = []
    soup = BeautifulSoup(html, "html.parser")

    review_container = soup.find("div", class_="js_product-reviews")

    if review_container is None:
        return []

    reviews = review_container.find_all("div", class_="js_product-review")

    if len(reviews) == 0:
        return []
    
    for review in reviews:
        id = review["data-entry-id"]
        user = review.find("span", class_="user-post__author-name").text.strip()
        score = float(review.find("span", class_="user-post__score-count").text.strip().replace("/5", "").replace(",", "."))
        
        date_wrapper = review.find("span", class_="user-post__published")
        date_arr = date_wrapper.findAll("time")

        publish_date = date_arr[0]["datetime"]
        usage_date = ""
        
        if len(date_arr) == 2:
            usage_date = date_arr[1]["datetime"]

        text = review.find("div", class_="user-post__text").text.strip()
 
        review_list.append(Review(id, user, score, publish_date, usage_date, text))
    
    pagination = soup.find("div", class_="pagination")

    if pagination is not None:
        pagination_next = pagination.find("a", class_="pagination__next")

        if pagination_next is not None:
            pagination_next_href = pagination_next["href"]
            response = get(f"https://www.ceneo.pl{pagination_next_href}", allow_redirects=False)
            return review_list + parseHtml(response.text)

    return review_list