# Avon String Quartet Planning Website

This website will allow us to effectively gather client event data before the performance has taken place as well as offer a plaform for clients to off feeback following the event.

View the live link [here]()

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
3. As a visiting user, I would like to edit my review, but not edit other's reviews.

### Write a Review Page

1. As a visiting user, I would like to write a review of the quartet's service at my past event. 
2. As a visiting user, I would like to see my review displayed on the review's page. 

### Add Details Page

1. As a visiting user, I would like to add details of my upcoming event to the database.
2. As a visiting user, I would like to view my details displayed on my wedding page.


## Features

### Navbar 

1. Navbar will be at the top of all pages on the desktop version once logged into the portal.
2. Navbar on desktop will display all options. On mobile, once the hamburger is clicked, the navigation options will appear.
3. Navbar will have the following options if logged in: 
    * My Wedding
    * Reviews
    * Log out 
3. Clicking on the relevant navigation option will redirect the user to that page.
 
 
### Log In Page

1. The Log In page will display the log in modal. It will be visually attractive with a photo of the quartet and define the colour scheme of the site.
2. It will feature a message at the bottom of the screen where the user can register their account if they don't have one already. 

### My Wedding Page

1. Once logged in, the user will be redirected to their profile. As a first time user, they will need to fill click on the "Add Details" form in order to input their event details.    
3. If they are a returning user, they will be able to view the details previously added or amend them by clicking the "Edit" button.


### Reviews Page 

1. Navigating to the Reviews page will display previously written reviews.
2. If the user is the author of the review, they will be able to edit the review.

### Write a Review Page 

1. Navigating to the Write a Review page will display the form to write a review.


## Design

### Colour Scheme 

Complementary shades of pale green dominant the scheme. The colours darken when buttons and options are hovered with the Materialize wave effect.

## Typography 

Open Sans was sourced from Google Fonts to create a clean, readable look. 

### Images 

The nav bar logo was taken from this [url](https://pixabay.com/vectors/bridge-nature-tree-lake-handdrawn-2497136/). Pixabay has many free images to choose from.

## Wireframes 

Wireframes can be viewed [here]().

### Technologies

## Languages Used

[HTML 5](https://en.wikipedia.org/wiki/HTML5) : HTML 5 was the main language used across the site.

[CSS 3](https://developer.mozilla.org/en-US/docs/Web/CSS) : CSS 3 was used to style the site.

[Javascript ES6](https://www.w3schools.com/js/js_es6.asp) : Javascript ES6 was used to manipulate the DOM in order to create the interactive game. 

### Frameworks Used

[Materialize](https://materializecss.com/) : Materialize was the main CSS framework used to create a grid system and responsive design for the site.

[Python3](https://www.python.org/) : Python3 was the main programming language used to create routes, models and logic in conjunction with Flask in order to render the site.

[Flask](https://flask.palletsprojects.com/en/2.1.x/) : Flask, the microweb framework, is used to link routes and models. THe code is written in Python3. 

[Jinja](https://flask.palletsprojects.com/en/2.1.x/) : Jinja is used to create templates to populate HTML pages on the site.

[Google Fonts](https://fonts.google.com/) : Google Fonts provided the font "Nanum Gothic" and "Gochi Hand" in order to customise and stylise the text. 

[Coolors](https://coolors.co/) : Coolors is a colour palette generator I used to create colours that worked together for the site.

[Git](https://git-scm.com/) : Git is the technology that hosts the Gitpod IDE and terminal where the project was coded. Git then committed and pushed the code to the cloud-based servers on GitHub.
 
[GitHub](https://github.com/) : GitHub hosted the project on its servers after being pushed by Git.

[Balsamiq](https://balsamiq.com/) : Balsamiq was used to create and download wireframes for the project.

[Favicon.io](https://favicon.io/favicon-converter/) : This website allowed me to generate a favicon for the site.

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) : Chrome Dev tools were utilised for the Javascript console as well as to verify the site's responsiveness and visual presentation. 

### Bugs 



## Testing 

### Code Validation 

The W3C Markup Validator, W3C CSS Validator and Jshint Services were used to check each page for syntax errors. 

[W3C Markup Validator](https://validator.w3.org/)

* []() - The validator flagged 
* []() - The validator flagged 
* []() - To fix this, I added some placeholder text and then added the hidden class from my CSS and then added some additional Javascript to remove this class when the game is started. The validator also notified me that lines 72 and 78 where I have section tags, I need to have heading elements to correspond. I changed these to div elements to rectify. I also forgot to close my section element on line 59. 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

[]()

[Jshint](https://jshint.com/) - 

## Manual Testing 

Manual tests were conducted throughout the development process via the python terminal in order to understand the UX, routing and data population features.

Deployment to Heroku was done in the beginning stages of development. 

### Test Cases based on User Stories

#### Login Page



#### My Wedding Page



#### Review Page



#### Write a Review and Edit Details Pages

## Deployment 

### Via Heroku 

1. Navigate to the Heroku link [here](https://github.com/samcat437/Milestone-2).
2. The Github reposity to view the code can be found [here](https://github.com/samcat437/Milestone-3).

### Via Gitpod

1. Navigate to the Github repository at [here](https://github.com/samcat437/Milestone-3).
2. Choose "Gitpod."
3. In the Bash terminal, type: `set_pg` and then `python3 app.py`
4. Choose "Make Public" when a blue button appears.
5. Choose "Open Browser" when the options appears.

### Acknowledgements

Massive thanks to my Code Institute mentor for guiding me through the development process. Thank you to tutor support for being patient during tutoring sessions. 