from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/adv-search")
def adv():
    return render_template("adv-search.html")

@app.route("/image-search")
def img_sr():
    return render_template("image-search.html")

if __name__ == '__main__':
    app.run()