from blog import db

class Article(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    author_img = db.Column(db.String())
    author_name = db.Column(db.String())
    reading_time = db.Column(db.Integer)


    def __repr__(self):
        return '<id {}>'.format(self.id)