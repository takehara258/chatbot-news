import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")


@app.route("/api/recommend_article")
def api_recommend_article():
    # 日経平均株価を取得
    with urlopen("https://finance.yahoo.co.jp/") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup(class_='ymuiEditLink mar0')
    item = items[0]
    return json.dumps({
        "content": item.string
    })


def main():
    app.run(debug=True, port=5004)


if __name__ == "__main__":
    main()
