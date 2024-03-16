class Product:
  def __init__(self, name):
    self.name = name

class Review:
  def __init__(self, id: str, user: str, score: float, publish_date: str, usage_date: str, text: str):
    self.id = id
    self.user = user
    self.score = score
    self.publish_date = publish_date
    self.usage_date = usage_date
    self.text = text
