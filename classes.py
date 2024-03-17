class Product:
  def __init__(self, name):
    self.name = name

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
