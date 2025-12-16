from flask import Flask, render_template, request

app = Flask(__name__)

# Simple AI recommendation logic
recommendations = {
    "ai": ["AI Chatbot", "Face Recognition System", "Smart Assistant"],
    "music": ["Music Recommendation App", "Mood-based Playlist AI"],
    "health": ["Health Monitoring AI", "Mental Health Chatbot"],
    "finance": ["Expense Tracker AI", "Fraud Detection System"],
    "education": ["AI Tutor", "Smart Learning Platform"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        interest = request.form["interest"].lower()
        result = recommendations.get(interest, ["No recommendations found"])
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
