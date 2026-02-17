from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
        session["history"] = []

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["attempts"] += 1
        session["history"].append(guess)

        if guess < session["number"]:
            message = "📉 Too low! Try again."
        elif guess > session["number"]:
            message = "📈 Too high! Try again."
        else:
            message = f"🎉 Correct! You guessed in {session['attempts']} attempts."
            session.pop("number")
            session.pop("attempts")
            session.pop("history")

    return render_template("index.html", message=message, history=session.get("history", []))

if __name__ == "__main__":
    app.run(debug=True)
