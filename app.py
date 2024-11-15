from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def is_daytime():
    hour = datetime.now().hour
    return 6 <= hour < 18

@app.route("/")
def home():
    day_mode = is_daytime()
    return render_template("index.html", day_mode=day_mode)

if __name__ == "__main__":
    app.run(debug=True)
