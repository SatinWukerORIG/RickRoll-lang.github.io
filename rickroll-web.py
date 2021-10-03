import markdown
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

def render_md(filename=""):
    with open(filename) as md_file:
        return markdown.markdown(md_file.read(), extensions=["fenced_code"])

@app.route("/", methods=["GET", "POST"])
def home():
    return render_md("home.md")

if __name__ == '__main__':
    app.run()