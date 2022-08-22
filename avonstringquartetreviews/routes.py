from flask import (
    flash, render_template,
    request, redirect, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from avonstringquartetreviews import app, db, mongo
from avonstringquartetreviews.models import Review, Details


@app.route("/")
def home():
    """
    The home function will run on opening the python file.
    Arguments: none
    The function returns the login.html page, passing isLogIn=True to the
    template.
    """
    return render_template("login.html", isLogIn=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    The register function will run when the register link on the login.html
    page is run.
    Arguments: none

    If the request method is post, then the function checks if the username is
        in the database.
        If so, a flash message informs the user and redirects to the the
        register function.
  
    If not, then the username and password are entered to the Mongodb database
    stored as register.

    The variable session["user"] is stored as a cookie taken from the username
        field entered in the form.

    A flash message appears on the my_wedding page once that is rendered from
        the redirected function
        and the username is passed as an argument.
  
    The function returns the register.html template.
    """
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

    return render_template("register.html", isLogIn=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    The login function does not take arguments. This function is called by the
        login page being generated.
    Arguments: none

    The function checks if there is a username appearing in the database
        already.
    It checks if the user has already entered their event details into the
        database and stores the outputs in variable respectively.
    If there is an existing user, it checks the password in the database
        matches the entered password.

    If the user has entered their details previously, it redirects to the
        my_wedding_details and passes username as the existing_user variable.
    If they haven't, it redirects to my_wedding and passes username as
        session["user"].

    If the username or password doesn't match, the user is notified there is
        an error and the function redirects to the login.

    The login template is returned, and isLogIn is passed for use in the jinja
        template logic.
    """
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

    return render_template("login.html", isLogIn=True)


@app.route("/my_wedding/<username>", methods=["GET", "POST"])
def my_wedding(username):
    """
    The my_wedding function is called if the user has not previous added event
        details.
    Arguments: username
    If the session["user"] is present, then render the my_wedding template.
    The function redirects to the login function.

    """
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
   
    if session["user"]:
        return render_template("my_wedding.html", username=username)
   
    return redirect(url_for("login"))


@app.route("/my_wedding_details")
def my_wedding_details():
    """
    The function will be called if the user has added details in the database
        previously.
    Arguments: none

    The wedding_details variable filters the list of details entered to
        matching that of the session user.
    The function returns the my_wedding_details template and passing this list
        and the username variable as arguments.
    """
    wedding_details = list(
        Details.query.order_by(
            Details.event_name).filter_by(username=session["user"]))

    return render_template(
        "my_wedding_details.html",
        wedding_details=wedding_details, username=session["user"])


@app.route("/reviews")
def reviews():
    """
    The function will take the list of reviews entered in the database and
        store it in a variable called reviews.
    Arguments: none

    It will render the reviews.html template and pass this variable.
    """
    reviews = list(Review.query.order_by(Review.review_name).all())
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    After the form is submitted, it will store the form data in the review
        variable and then add it to the postgresql database session.
    It will then commit the changes and redirect to the review function.
    Arguments: none
    It returns the render template for the add_review.html page.
    """
    if request.method == "POST":
        review = Review(
            review_name=request.form.get("review_name"),
            review_first_name=request.form.get("first_name"),
            review_last_name=request.form.get("last_name"),
            review_date=request.form.get("wedding_date"),
            review_email=request.form.get("email"),
            review_venue=request.form.get("venue"),
            review_content=request.form.get("review_content"),
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("reviews")) 
    return render_template("add_review.html")


@app.route("/add_details", methods=["GET", "POST"])
def add_details():
    """
    After the form is submitted, it will store the form data in the details
        variable and then add it to the postgresql database session.
    It will then commit the changes and redirect to the my_wedding_details
        function, passing detailsAdded as truthy.
    Arguments: none
    It returns the render template for the add_details.html page.
    """
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
        return redirect(url_for("my_wedding_details", detailsAdded=True))
    return render_template("add_details.html")


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    The function will query Review and retrieve review_id and store it as the
        variable review.
    Once the button is pressed, if the method is post, the function will
        request the four input fields and store them as variables.
    These are then passed the the database session and committed.
    Then the function redirects to the reviews function.
    Arguments: review_id
    The function returns the edt_review.html template and passes review as
        review queried in the first line.
    """
    review = Review.query.get_or_404(review_id)
    if request.method == "POST": 
        review.review_name = request.form.get("review_name")
        review.review_date = request.form.get("wedding_date")
        review.review_venue = request.form.get("venue")
        review.review_content = request.form.get("review_content")
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_review.html", review=review)


@app.route("/edit_details/<int:details_id>", methods=["GET", "POST"])
def edit_details(details_id):
    """
    The function will query Details and retrieve details_id and store it as the
        variable wedding_details.
    Once the button is pressed, if the method is post, the function will
        request the six input fields and store them as variables.
    These are then passed the the database session and committed.
    Then the function redirects to the my_wedding_details function.
    Arguments: details_id
    The function returns the edt_details.html template and passes
    wedding_details as wedding_details queried in the first line.
    """
    wedding_details = Details.query.get_or_404(details_id)
    if request.method == "POST":
        wedding_details.event_name = request.form.get("event_name")
        wedding_details.event_date = request.form.get("wedding_date")
        wedding_details.event_venue = request.form.get("venue")
        wedding_details.event_start = request.form.get("start_time")
        wedding_details.event_end = request.form.get("end_time")
        wedding_details.event_content = request.form.get("event_content")
        db.session.add(wedding_details)
        db.session.commit()
        return redirect(url_for(
            "my_wedding_details", wedding_details=wedding_details))
    return render_template(
        "edit_details.html", wedding_details=wedding_details)


@app.route("/delete_review_confirmation")
def delete_review_confirmation():
    """
    This function takes no arguments and redirects to the reviews function,
        passing review as review queried in that function.
    """
    return redirect(url_for("reviews", review=review))


@app.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    """
    The function defines review by querying Review.
    It then deletes if from the session and commits.
    Arguments: review_id
    It is redirects the reviews function.
    """
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("reviews"))


@app.route("/delete_details_confirmation")
def delete_details_confirmation():
    """
    This function may not be called except if there is a bug, as the user's
        profile should only render their own entered event data.
    It defines author as the session user and then admin of the event details
        the username entered in the database.
    If they do not match, the user will be notified.
    Arguments: none
    The function returns the my_wedding_details function, passing
        wedding_details as previously defined wedding_details.
    """
    author = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    admin = Details.query.get_or_404(username)
    if author != admin:
        flash("You can can only edit your own review.")
    return redirect(url_for(
        "my_wedding_details", wedding_details=wedding_details))


@app.route("/delete_details/<int:details_id>")
def delete_details(details_id):
    """
    The function defines wedding_details by querying Details.
    It then deletes if from the session and commits.
    Arguments: details_id
    It is redirects the my_wedding function.
    """
    wedding_details = Details.query.get_or_404(details_id)
    db.session.delete(wedding_details)
    db.session.commit()
    return redirect(url_for("my_wedding", username=session["user"]))


@app.route("/logout")
def logout():
    """
    The function logs the user out by removing them from the session. The user
        will be notified.
    The function redirects to the login function.
    """
    session.pop("user", None)
    flash("You are now logged out")
    return redirect(url_for("login"))
