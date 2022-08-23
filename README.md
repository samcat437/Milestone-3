# Avon String Quartet Planning Website

This website will allow us to effectively gather client event data before the performance has taken place as well as offer a platform for clients to off feedback following the event.

View the live link [here](https://avon-string-quartet-reviews.herokuapp.com/)

# User Experience

## User Stories

### Log In Page

1. As a visiting user, I would like to log into the portal.
2. As a visiting user, if I don't have an account yet, I would like to register.

### My Wedding Page

1. As a visiting user, I would like to be able to navigate to different sections of the portal and it display data related to my login credentials. 
2. As a visiting user, I would like to be welcomed to my profile page.
3. As a visiting user, I would like to add details regarding my event and see it displayed in on my profile. 
4. As a returning user, I will be able to view the details I have added previously.
5. As a returning user, I will be able to edit the details I have added previously.

### Review Page

1. As a visiting user, I would like to view previous reviews submitted into the database. 
2. As a visiting user, I would like to be able to add a review.
3. As a visiting user, I would like to be able to edit or delete a review.

### Write a Review Page

1. As a visiting user, I would like to write a review of the quartet's service at my past event. 
2. As a visiting user, I would like to see my review displayed on the review's page. 

### Add Details Page

1. As a visiting user, I would like to add details of my upcoming event to the database.
2. As a visiting user, I would like to view my details displayed on my wedding page.

### Log Out
1. As a visiting user, I would like to sign out of the account and be taken back to the login page.


## Features

### Navbar and Footer

1. Navbar will be at the top of all pages on the desktop version once logged into the portal.
2. Navbar on desktop will display all options. On mobile, once the hamburger is clicked, the navigation options will appear.
3. Navbar will have the following options if logged in: 
    * My Wedding
    * Reviews
    * Log out 
3. Clicking on the relevant navigation option will redirect the user to that page.

4. Footer will be sticky. Navbar will be responsive and fill the entire width of small screens.
 
 
### Log In Page

1. The Log In page will display the login form. It will be visually attractive by defining the colour scheme of the site.
2. It will feature a message at the bottom of the screen where the user can register their account if they don't have one already. 

### My Wedding Page

1. Once logged in, the user will be redirected to their profile. As a first-time user, they will need to fill click on the "Add Details" form in order to input their event details.    
3. If they are a returning user, they will be able to view the details previously added or amend them by clicking the "Edit" button.

### Reviews Page 

1. Navigating to the Reviews page will display previously written reviews.
2. If the user is the author of the review, they will be able to edit the review.

### Write a Review and Add Details Pages

1. Navigating to the Write a Review and Add Details page will display the form to write a review.


## Design

### Colour Scheme 

Complementary shades of pale green dominant the scheme. The colours darken when buttons and options are hovered with the Materialize wave effect.

## Typography 

Open Sans was sourced from Google Fonts to create a clean, readable look. 

### Images 

The navbar logo was taken from this [url](https://pixabay.com/vectors/bridge-nature-tree-lake-handdrawn-2497136/). Pixabay has many free images to choose from, including the background image displayed across the site.

## Wireframes 

Wireframes were created at project inception and do not totally represent what ended up being created. They can be viewed [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/wireframes/Milestone-3.pdf).

### Technologies

## Languages Used

[HTML 5](https://en.wikipedia.org/wiki/HTML5) : HTML 5 was the main language used across the site.

[CSS 3](https://developer.mozilla.org/en-US/docs/Web/CSS) : CSS 3 was used to style the site.

[Javascript ES6](https://www.w3schools.com/js/js_es6.asp) : Javascript ES6 was used to manipulate the DOM in order to create the interactive game. 

### Frameworks Used

[Materialize](https://materializecss.com/) : Materialize was the main CSS framework used to create a grid system and responsive design for the site.

[Python3](https://www.python.org/) : Python3 was the main programming language used to create routes, models and logic in conjunction with Flask in order to render the site.

[Flask](https://flask.palletsprojects.com/en/2.1.x/) : Flask, the microweb framework, is used to link routes and models. The code is written in Python3. 

[Jinja](https://flask.palletsprojects.com/en/2.1.x/) : Jinja is used to create templates to populate HTML pages on the site.

[Google Fonts](https://fonts.google.com/) : Google Fonts provided the font "Nanum Gothic" and "Gochi Hand" in order to customise and stylise the text. 

[Coolors](https://coolors.co/) : Coolors is a colour palette generator I used to create colours that worked together for the site.

[Git](https://git-scm.com/) : Git is the technology that hosts the Gitpod IDE and terminal where the project was coded. Git then committed and pushed the code to the cloud-based servers on GitHub.
 
[GitHub](https://github.com/) : GitHub hosted the project on its servers after being pushed by Git.

[Balsamiq](https://balsamiq.com/) : Balsamiq was used to create and download wireframes for the project.

[Fontawesome](https://fontawesome.com/kits) : Font Awesome is a database of icons that can be used for visual interest.

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) : Chrome Dev tools were utilised for the Javascript console as well as to verify the site's responsiveness and visual presentation. 

### Bugs 

This project was very difficult for me, especially with a busy summer work schedule. I was initially slowed down due to having to install flask migrate software, which wasn't covered in the course. The tutors helped me implement this as the when I updated my model and tried to create the database, I could not overwrite it. 

I then had trouble creating a model that would display flash messages. I then tried toasts, but I couldn't figure out how to implement the Javascript with jinja. I eventually reverted to the simple h4, just so that the messages would come through. I spent a lot of time getting the models to work for the confirmation messages of the delete functions. Thankfully they seem functional.

One bug I didn't squash that I wanted to but ran out of time was that if the user doesn't submit event details and then navigate towards another page and then return, the app will display the my_wedding_details page rather than the my_wedding page. I tried to fix by passing in an detailsAdded argument when the redirect function was called and then using jinja logic, but it didn't work, so I deleted it. Also, if you are a returning user and have deleted your details, it is displaying my_wedding_details rather than wedding_details. More logic is needed and will be added in future builds.

I also was not able to add the admin logic to stop the ability to edit or delete other's reviews before submission. This will be a future feature.

The h4 flash messages have also ruined the padding a bit, which you can see in the test screenshot on the log out page. If in the future I can get the modals to work, this will improve the user experience.

## Testing 

### Code Validation 

The W3C Markup Validator, W3C CSS Validator and Jshint Services were used to check each page for syntax errors. 

[W3C Markup Validator](https://validator.w3.org/)

* [login.html](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/login.png) - The validator flagged a stray section tag. This was inherited from base.html and was valid there, so I ignored this error.
* [reviews.html](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/reviews.png) - The validator flagged more inherited base.html elements that are valid. This was the same for the register.html page and add_details.html pages.
* [edit_review.html](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/edit_review.png) - The validator brought a typo of the minlength attribute to my attention.
* [edit_details.html](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/edit_details.png) - The validator flagged that a textarea could not have a value attribute. 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

[style.css](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/css.png) - This passed with no issues.

[Jshint](https://jshint.com/) 

[script.js](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/javascript.png) - As my javascript was only the initialisation code from Materialize, I am able to ignore these warnings. 

[Pep8online](http://pep8online.com/)

[env.py](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/env.py.png) - The validator was stating that the line was too long, but when I "fixed" this, it broke my Heroku app. Slack answers showed I could ignore this.

[__init__.py](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/__init__.py.png) - This passed as did app.py.

[routes.py](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/code-validation/routes.py.png) - Routes.py was a bit trickier. I fixed all the red errors, and then went to work on eliminating whitespace. However, when I did the last ones, there was no way to delete whitespace without messing up the tabbing which is essential. It seems functional, so I hope leaving it like it is will be ok. 

## Manual Testing 

Manual tests were conducted throughout the development process via the python terminal to understand the UX, routing and data population features.

Deployment to Heroku was done in the beginning stages of development, but then left it late, and I had forgotten what needed updating. I had a bit of a hard time getting it deployed before the deadline but eventually got there with tutor support pointing out that my env.py file wasn't matching config vars. I then needed to open the command line in Heroku and create the postgresql databases.

### Test Cases based on User Stories

#### Login Page

1. As a visiting user, I would like to log into the portal.
* I successfully logged in as an existing user [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/logged%20in.png)

2. As a visiting user, if I don't have an account yet, I would like to register.
* I successfully logged in as a new user [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/registered-user.png)

#### My Wedding Page

1. As a visiting user, I would like to be able to navigate to different sections of the portal and it display data related to my login credentials. 
* I can view my details that I added here on my_weddings [page](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/my_wedding.png)
* I can view my review that I added here on the review [page](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/reviews-page.png)

2. As a visiting user, I would like to be welcomed to my profile page.
* After logging in, I am directed [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/logged%20in.png) with a message.

3. As a visiting user, I would like to add details regarding my event and see it displayed in on my profile. 
* I can see this in point 1.

4. As a returning user, I will be able to view the details I have added previously.
* I will be directed to my profile page when I return like [this](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/my_wedding.png)

5. As a returning user, I will be able to edit the details I have added previously.
* I can do this by clicking on the edit button.

#### Review Page

1. As a visiting user, I would like to view previous reviews submitted into the database. 
* I don't just see my own by other ones [too](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/reviews-page.png)

2. As a visiting user, I would like to be able to add a review. 
* I can add as many revies as I want right now and see them displayed. 

#### Write a Review Page

1. As a visiting user, I would like to write a review of the quartet's service at my past event. 
* I wrote a review by filling out the form [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/add_review.png)

2. As a visiting user, I would like to see my review displayed on the review's page. 
* I can see this on the reviews [page](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/reviews-page.png)

#### Add Details Page

1. As a visiting user, I would like to add details of my upcoming event to the database.
* I added details by filling out the form [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/filling-add-form-1.png). 

2. As a visiting user, I would like to view my details displayed on my wedding page.
* I can see this on my_wedding [page](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/my_wedding.png)

#### Log Out
1. As a visiting user, I would like to sign out of the account and be taken back to the login page.
* I have logged out [here](https://github.com/samcat437/Milestone-3/blob/main/avonstringquartetreviews/docs/test-screenshots/logged-out.png)

## Code

Much of the logic was taken from the Code Institute Taskmanager Walkthrough project, which I was advised by my mentor that was fine to do. I also used Materialize framework nav, footer, modal and classes for responsive design.

## Deployment 

### Via Heroku 

I used Heroku.com to host my app. This website ran the python code and produced a live link which can be found [here](https://avon-string-quartet-reviews.herokuapp.com/). Heroku connects to GitHub and with every push, updates the site on Heroku.

1. In the gitpod terminal, a requirements.txt and a Procfile were first created by using the following commands:
pip3 freeze –local > requirements.txt and echo web: python app.py > Procfile
2. The new files are then committed to GitHub.
3. In Heroku.com, a new account is created, followed by a new app. Europe was then chosen as the region nearest geographically for free service. Amazon Web Services were also chosen as the provider.
4. Next, the Deployment Method of Connecting to GitHub is selected.
Within the search bar, the repository name is entered and the correct repository is selected to connect via the button. Automatic deploys are enabled from the main branch.
5. In the settings tab, the Config Vars information needed to be filled out very carefully. If these contain discrepencies, the app will not run. These included the following fields: DATABASE_URL, HEROKU_POSTGRESQL_RED_URL, IP, MONGO_DBNAME, MONGO_URI, PORT and SECRET_KEY. These fields correspond to the respective MongoDB, Heroku Postgresql add-on, Port and IP information as appropriate for your project.
6. "Deploy Branch" was selected and the app is successfully built. 

### Via Gitpod ran locally

1. Navigate to the Github repository at [here](https://github.com/samcat437/Milestone-3).
2. Choose "Gitpod."
3. In the Bash terminal, type: `python3 app.py`
4. Choose "Make Public" when a blue button appears.
5. Choose "Open Browser" when the options appears.

### Acknowledgements

Massive thanks to my Code Institute mentor for guiding me through the development process. Thank you to tutor support for being patient during tutoring sessions. 