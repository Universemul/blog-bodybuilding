from blog import db
from models import Article, Author

def create_all():
    db.create_all()

def create_article(author: Author):
    a = Article(
        title="test david", 
        description="Ceci est une description", 
        reading_time=6,
        author_id=author.id
    )
    db.session.add(a)
    db.session.commit()

def create_author():
    a = Author(
        name="David",
        description="Bonjour, je suis un auteur",
    )
    db.session.add(a)
    db.session.commit()
    return a