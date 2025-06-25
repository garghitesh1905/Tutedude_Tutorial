from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


# MongoDB Atlas connection
client = MongoClient("mongodb+srv://dummy:12345@cluster0.1neikzf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["your_database"]
collection = db["your_collection"]

@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    name = email = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        # Basic validation
        if not name or not email:
            error = "Name and email are required."
            return render_template("form.html", error=error, name=name, email=email)

        # Insert into MongoDB
        try:
            collection.insert_one({"name": name, "email": email})
            return redirect("/success")  
        except Exception as e:
            error = "Database error: " + str(e)
            return render_template("form.html", error=error, name=name, email=email)

    return render_template("form.html", error=error, name=name, email=email)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route('/todo', methods=['GET'])
def todo_form():
    return render_template('todo.html')

if __name__ == "__main__":
    app.run(debug=True)
