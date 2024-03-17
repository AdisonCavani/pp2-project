class Review:
  def __init__(self, id: str, user: str, recommendation: bool, score: float, verified: bool, publish_date: str, usage_date: str, likes: int, dislikes: int, text: str, adv: list[str], disadv: list[str]):
    self.id = id
    self.user = user
    self.recommendation = recommendation
    self.score = score
    self.verified = verified
    self.publish_date = publish_date
    self.usage_date = usage_date
    self.likes = likes
    self.dislikes = dislikes
    self.text = text
    self.adv = adv
    self.disadv = disadv

class Product:
  def __init__(self, id: str, name: str, img: str, review_count: int, adv_count: int, disadv_count: int, avg_score: float, reviews: list[Review], reviews_json: str):
    self.id = id
    self.name = name
    self.img = img
    self.review_count = review_count
    self.adv_count = adv_count
    self.disadv_count = disadv_count
    self.avg_score = avg_score
    self.reviews = reviews
    self.reviews_json = reviews_json

class ProductInfo:
  def __init__(self, id: str, name: str, img: str):
    self.id = id
    self.name = name
    self.img = img