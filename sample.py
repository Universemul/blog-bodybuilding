from blog import db
from models import Article

def create_all():
    db.create_all()

def create_article():
    a = Article(title="test david", description="Ceci est une description", author_img="https://www.gravatar.com/avatar/e56154546cf4be74e393c62d1ae9f9d4?s=250&amp;d=mm&amp;r=x", author_name="David", reading_time=6)
    db.session.add(a)
    db.session.commit()