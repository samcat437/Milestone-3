from flask import (
    flash, render_template, request, redirect, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from avonstringquartetreviews import app, db, mongo
from avonstringquartetreviews.models import Review, Users



# def home():
#     return render_template("reviews.html")

@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = Review(
            review_name=request.form.get("review_name"),
            review_first_name=request.form.get("review_first_name"),
            review_last_name=request.form.get("review_last_name"),
            review_date=request.form.get("review_date"),
            review_email=request.form.get("review_email"),
            review_venue=request.form.get("review_venue"),
            review_content=request.form.get("review_venue")
        )
        db.session.add(review)
        db.session.commit()
        # not redirecting 
        return redirect(url_for("home")) 
    return render_template("add_review.html")


@app.route("/login")
def login(): 
    return render_template("login.html")


@app.route("/my_wedding")
def my_wedding(): 
    return render_template("my_wedding.html")