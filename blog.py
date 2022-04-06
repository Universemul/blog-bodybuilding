from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['BLOG_CONFIG'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Article

@app.route("/")
def main():
    articles = Article.query.options(db.joinedload(Article.author)).all()
    formatted_articles = [
        build_formatted_article(a)
        for a in articles
    ]
    return render_template("index.html", articles=formatted_articles)

@app.route("/articles/<article_id>")
def get_article(article_id: str):
    if not article_id.isdigit():
        return render_template("index.html", articles=Article.query.all())
    article = Article.query.options(db.joinedload(Article.author)).get(int(article_id))
    return render_template("article.html", article=build_formatted_article(article))

def build_formatted_article(article: Article):
    return {
        'id': article.id,
        'description': article.description,
        'title': article.title,
        'reading_time': article.reading_time,
        'created_date': article.created_date.strftime("%d %B, %Y"), #format needed
        'author_img': article.author.img,
        'author_name': article.author.name,
        'author_description': article.author.description
    }