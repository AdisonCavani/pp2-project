from bs4 import BeautifulSoup
from requests import get
from classes import Review

def parse_html(html: str) -> list[Review]:
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
        recommendation = review.find("span", class_="user-post__author-recomendation") is not None
        score = float(review.find("span", class_="user-post__score-count").text.strip().replace("/5", "").replace(",", "."))
        verified = review.find("div", class_="review-pz") is not None
        date_wrapper = review.find("span", class_="user-post__published")
        date_arr = date_wrapper.findAll("time")

        publish_date = date_arr[0]["datetime"]
        usage_date = ""
        
        if len(date_arr) == 2:
            usage_date = date_arr[1]["datetime"]
        
        likes = int(review.find("button", class_="vote-yes")["data-total-vote"])
        dislikes = int(review.find("button", class_="vote-no")["data-total-vote"])
        text = review.find("div", class_="user-post__text").text.strip()
        
        adv = []
        disadv = []

        feature_wrapper = review.findAll("div", class_="review-feature__col")

        if feature_wrapper is not None:
            for idx, div in enumerate(feature_wrapper):
                if idx == 0:
                    adv_wrapper = div.findAll("div", class_="review-feature__item")
                    for adv_node in adv_wrapper:
                        adv.append(adv_node.text.strip())
                elif idx == 1:
                    disadv_node = div.findAll("div", class_="review-feature__item")
                    for disadv_node in disadv_node:
                        disadv.append(disadv_node.text.strip())
 
        review_list.append(Review(id, user, recommendation, score, verified, publish_date, usage_date, likes, dislikes, text, adv, disadv))
    
    pagination = soup.find("div", class_="pagination")

    if pagination is not None:
        pagination_next = pagination.find("a", class_="pagination__next")

        if pagination_next is not None:
            pagination_next_href = pagination_next["href"]
            response = get(f"https://www.ceneo.pl{pagination_next_href}", allow_redirects=False)
            return review_list + parse_html(response.text)

    return review_list
