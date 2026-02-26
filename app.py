from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# 投稿データを保存するリスト
posts = [
    {"name": "管理人", "message": "掲示板へようこそ！", "date": "2026/02/26 15:00:00"}
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post", methods=["POST"])
def post():
    name = request.form.get("name") or "名無しさん"
    message = request.form.get("message")
    if message:
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        posts.append({"name": name, "message": message, "date": date})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
