from flask import Blueprint, render_template, request
from bs4 import BeautifulSoup
from requests import get
from classes import Review
from utils import parseHtml

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
        return render_template("pages/product.html", data=parseHtml(response.text), len=len)
    
    return render_template("pages/404.html")

@bp.route("/product-list")
def product_list():
    return render_template("pages/product-list.html")
