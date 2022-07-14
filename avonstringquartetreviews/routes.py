from flask import (
    flash, render_template, request, redirect, session, url_for)
# from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, check_password_hash
from avonstringquartetreviews import app, db, mongo
from avonstringquartetreviews.models import Review 


@app.route("/")
def home():
    return render_template("reviews.html")

# not working
@app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(Review.review_name).all())
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = Review(
            review_name=request.form.get("review_name"),
            review_first_name=request.form.get("first_name"),
            review_last_name=request.form.get("last_name"),
            review_date=request.form.get("wedding_date"),
            review_email=request.form.get("email"),
            review_venue=request.form.get("venue"),
            review_content=request.form.get("review_content")
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("reviews")) 
    return render_template("add_review.html")


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id): 
    review = Review.query.get_or_404(review_id)
    if request.method == "POST": 
        review.review_name = request.form.get("review_name")
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_review.html", review=review)


@app.route("/login")
def login(): 
    return render_template("login.html")


@app.route("/my_wedding")
def my_wedding(): 
    return render_template("my_wedding.html")