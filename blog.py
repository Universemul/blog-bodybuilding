from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def main():
    articles = []
    for i in range (1, 30):
        article = {
            'title': f"Test {i}",
            'description': "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
            'author_img': "https://www.gravatar.com/avatar/e56154546cf4be74e393c62d1ae9f9d4?s=250&amp;d=mm&amp;r=x",
            'author_name': "Steve",
            'reading_time': i
        }
        articles.append(article)
    return render_template("index.html", articles=articles)