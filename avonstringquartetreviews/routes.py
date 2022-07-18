from flask import (
    flash, render_template, 
    request, redirect, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from avonstringquartetreviews import app, db, mongo
from avonstringquartetreviews.models import Review, Details


@app.route("/")
def home():
    return render_template("my_wedding.html")

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
        # checks if user has entered in Details db
        details_added = list(Details.query.order_by(Details.event_name).all())
        
        if existing_user: 
            # ensure hashed password matches import
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()

                    # if has user credentials and has entered in Details db
                    if session["user"] and details_added: 
                        return redirect(url_for(
                        "my_wedding_details", username=existing_user))
                    else: 
                        flash("Hi, {}.".format(request.form.get("username")))
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

    return render_template("login.html", isLogIn = True)


@app.route("/my_wedding/<username>", methods=["GET", "POST"])
def my_wedding(username): 
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("my_wedding.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/my_wedding_details")
def my_wedding_details():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    wedding_details = list(Details.query.order_by(Details.event_name).all())
    # error ask Rohit
    # if Details.event_name not in wedding_details:
    #     return render_template("my_wedding.html", username=username)
    return render_template(
        "my_wedding_details.html", wedding_details=wedding_details, username=username)


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


@app.route("/add_details", methods=["GET", "POST"])
def add_details():
    if request.method == "POST":
        details = Details(
            username=session["user"],
            event_name=request.form.get("event_name"),
            event_first_name=request.form.get("first_name"),
            event_last_name=request.form.get("last_name"),
            event_date=request.form.get("wedding_date"),
            event_email=request.form.get("email"),
            event_venue=request.form.get("venue"),
            event_start=request.form.get("start_time"),
            event_end=request.form.get("end_time"),
            event_content=request.form.get("event_content")
        )
        db.session.add(details)
        db.session.commit()
        return redirect(url_for("my_wedding_details"))
    return render_template("add_details.html")


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    if request.method == "POST": 
        review.review_name = request.form.get("review_name")
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_review.html", review=review)


@app.route("/edit_details/<int:details_id>", methods=["GET", "POST"])
def edit_details(details_id):
    wedding_details = Details.query.get_or_404(details_id)
    if request.method == "POST": 
        wedding_details.event_name = request.form.get("event_name")
        db.session.commit()
        return redirect(url_for("my_wedding_details"))
    return render_template(
        "edit_details.html", wedding_details=wedding_details)


@app.route("/delete_review_confirmation")
def delete_review_confirmation(admin):
    # pseudo code for checking if you are the author of the review 
    if admin != session["_id"]:
        flash("You can only delete your own reviews.")
    return redirect(url_for("reviews", review=review))


@app.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("reviews"))


@app.route("/delete_details_confirmation")
def delete_details_confirmation():
    return redirect(url_for("my_wedding_details", wedding_details=wedding_details))


@app.route("/delete_details/<int:details_id>")
def delete_details(details_id):
    wedding_details = Details.query.get_or_404(details_id)
    db.session.delete(wedding_details)
    db.session.commit()
    return redirect(url_for("my_wedding_details"))


@app.route("/logout")
def logout():
    print("Hello")
    session.pop("user", None)
    flash("You are now logged out")
    return redirect(url_for("login"))
