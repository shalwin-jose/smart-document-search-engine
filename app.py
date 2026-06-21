from flask import Flask, render_template,request
from main import get_search_results
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        user_query = request.form.get("user_query")
        selected_type = request.form.get("search_type")

        search_scores=get_search_results(user_query, search_type=selected_type)

        return render_template("index.html",message=f"Results for:'{user_query}' (Using {selected_type} engine)",results=search_scores)
    return render_template(
        "index.html",
        message="Search engine logic is ready!", 
        results=None)

if __name__ == "__main__":
    app.run(debug=True)