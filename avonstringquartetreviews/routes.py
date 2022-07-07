from flask import render_template, request, redirect, url_for
from avonstringquartetreviews import app, db
from avonstringquartetreviews.models import Review


@app.route("/")
def home():
    return render_template("reviews.html")


@app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(Review.review_venue).all())
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
        return redirect(url_for("reviews")) 
    return render_template("add_review.html")