from avonstringquartetreviews import db


class Review(db.Model):
    # schema for the Review model
    id = db.Column(db.Integer, primary_key=True)
    review_name = db.Column(db.String(25), unique=True, nullable=False)
    review_first_name = db.Column(db.String(25), unique=True, nullable=False)
    review_last_name = db.Column(db.String(25), unique=True, nullable=False)
    review_email = db.Column(db.String(25), unique=True, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    review_venue = db.Column(db.String(25), unique=False)
    review_content = db.Column(db.Text, nullable=False)


    def __repr__(self): 
        # __repr__ to represent itself in the form of a string
        return "#{0} - Review: {1} | Date: {2}".format(
            self.id, self.review_name, self.review_date
        )
        