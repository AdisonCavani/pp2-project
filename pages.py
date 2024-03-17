import json
from flask import Blueprint, render_template, request
from requests import get
from classes import Product
from utils import parse_product, parse_reviews

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/product")
def product():
    product_id = request.args.get("id")

    if not product_id:
        return render_template("pages/product.html", data=None)
    
    response = get(f"https://www.ceneo.pl/{product_id}#tab=reviews", allow_redirects=False)

    if response.status_code == 200:
        data = parse_reviews(response.text)
        dataJson = json.dumps(data, default = lambda x: x.__dict__)
        return render_template("pages/product.html", data=data, dataJson=dataJson, len=len)
    
    return render_template("pages/404.html")

@bp.route("/product-stats", methods=["POST"])
def product_stats():
    data = request.form["data"]
    return render_template("pages/product-stats.html", data=data)


@bp.route("/product-list")
def product_list():
    products_idx = ["30976453", "158184470", "157746229", "157746229", "158184470", "30976453"]
    products: list[Product] = []

    for product_id in products_idx:
        response = get(f"https://www.ceneo.pl/{product_id}#tab=reviews", allow_redirects=False)

        if response.status_code == 200:
            product = parse_product(response.text)

            reviews = parse_reviews(response.text)
            reviews_json = json.dumps(reviews, default = lambda x: x.__dict__)

            review_count = len(reviews)
            adv_count = sum(len(review.adv) for review in reviews)
            disadv_count = sum(len(review.disadv) for review in reviews)
            total_score = sum(review.score for review in reviews)
            avg_score = round(total_score / review_count if review_count > 0 else 0)

            products.append(Product(
                product.id,
                product.name,
                product.img,
                review_count,
                adv_count,
                disadv_count,
                avg_score,
                reviews,
                reviews_json)
            )
        else:
            return render_template("pages/404.html")
    
    return render_template("pages/product-list.html", products=products)
