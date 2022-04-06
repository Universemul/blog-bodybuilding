from blog import db
from sqlalchemy.sql import func

class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    reading_time = db.Column(db.Integer)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Author(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    img = db.Column(db.String(), default="https://www.gravatar.com/avatar/e56154546cf4be74e393c62d1ae9f9d4?s=250&amp;d=mm&amp;r=x")
    joined_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    articles = db.relationship('Article', backref='author', lazy=True)


    def __repr__(self):
        return '<id {}>'.format(self.id)