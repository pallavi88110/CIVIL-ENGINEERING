from flask import Flask, render_template, request
import os
from analyzer import analyze_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["image"]

        if file.filename == "":
            return "No file selected"

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        report = analyze_image(filepath)

        return render_template("result.html", image=filepath, report=report)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
