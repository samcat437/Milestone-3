from flask import (
    flash, render_template, 
    request, redirect, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from avonstringquartetreviews import app, db, mongo
from avonstringquartetreviews.models import Review


@app.route("/")
def home():
    return render_template("reviews.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("review.html", reviews=reviews)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user: 
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("my_wedding", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user: 
            # ensure hashed password matches import
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hi, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "my_wedding", username=session["user"]))
            else: 
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else: 
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user", None)
    flash("You are now logged out")
    return redirect(url_for("login"))
    

@app.route("/my_wedding/<username>", methods=["GET", "POST"])
def my_wedding(username): 
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("my_wedding.html", username=username)
    
    return redirect(url_for("login"))

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


@app.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("reviews"))
