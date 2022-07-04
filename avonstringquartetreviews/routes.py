from flask import render_template
from avonstringquartetreviews import app, db
from avonstringquartetreviews.models import Review


@app.route("/")
def home():
    return render_template("reviews.html")