from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        user_query = request.form["user_query"]

        return render_template(
            "index.html",
            message=user_query
        )

    return render_template("index.html",message="Search engine logic is ready!")
if __name__ == "__main__":
    app.run(debug=True)