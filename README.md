# Avon String Quartet Planning Website

This website will allow us to effectively gather client event data before the performance has taken place as well as offer a plaform for clients to off feeback following the event.

View the live link [here]()

# User Experience

## User Stories

### Log In Page

1. As a visiting user, I would like to log into the portal.
2. As a visiting user, if I don't have an account yet, I would like to register.

### My Wedding Page

1. As a visiting user, I would like to be able to navigate to different sections of the portal. 
2. As a visiting user, I would like to be welcomed to my profile page.
3. As a visiting user, I would like to add details regarding my event and see it displayed in on my profile. 
4. As a returning user, I will be able to view the details I have added previously.
5. As a returning user, I will be able to edit the details I have added previously.

### Review Page

1. As a visiting user, I would like to view previous reviews submitted into the database. 
2. As a visiting user, I would like to add a review. 
3. As a visiting user, I would like to edit my review, but not edit other's reviews.

## Features

### Navbar 

1. Navbar will be at the top of all pages on the desktop version once logged into the portal.
2. Navbar on desktop will display all options. On mobile, once the hamburger is clicked, the navigation options will appear.
3. Navbar will have the following options if logged in: 
    * My Wedding
    * Reviews
    * Log out 
3. Clicking on the relevant navigation option will redirect the user to that page.
4. Navbar will be sticky on the lesson page.
 
 
### Log In Page

1. The Log In page will display the log in modal. It will be visually attractive with a photo of the quartet and define the colour scheme of the site.
2. It will feature a message at the bottom of the screen where the user can register their account if they don't have one already. 

### My Wedding Page

1. Once logged in, the user will be redirected to their profile. As a first time user, they will need to fill click on the "Add Details" form in order to input their event details.    
3. If they are a returning user, they will be able to view the details previously added or amend them by clicking the "Edit" button.


### Reviews Page 

1. Navigating to the Reviews page will display previously written reviews.
2. If the user is the author of the review, they will be able to edit the review.

## Design

### Colour Scheme 

Contrast colours of pale blue, pale pink and pale green dominant the scheme. The colours darken when buttons and options are hovered, as well as the buttons expanding. 

## Typography 

For paragraph text, Nanum Gothic sourced from Google Fonts is used to create a modern and fun look as the site is designed for educational purposes. Sans-serif is the fallback option.

For headings and the nav bar, Gochi Hand from Google Fonts to emphasise the whimsical nature of the site. 

### Images 

Images were used from the free site : [pixabay](https://pixabay.com) and then cropped for use across the site. The examples in the quiz and in the nav bar were cropped from this [image](https://pixabay.com/vectors/key-signatures-keys-music-notation-6792283/).

The nav bar was taken from this [one](https://pixabay.com/vectors/music-treble-clef-musical-symbol-39881/).

The backgrounds were taken from these links : [index.html background](https://pixabay.com/vectors/cloud-speech-bubble-thinking-idea-146176/) and [game.html background](https://pixabay.com/vectors/clouds-pattern-wallpaper-sky-5930599/).

## Wireframes 

Wireframes can be viewed [here](https://github.com/samcat437/Milestone-2/blob/main/docs/Wireframes/keysignatures.pdf).

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

[Colorzilla](https://www.colorzilla.com/gradient-editor/) : Colorzilla has an ultimate CSS gradient generator that I used to generate the CSS for the background colours of my lesson.html page. 

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

* [index.html](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/index.html%20W3C%20markup%20-%20AAKS.png) - The validator flagged that my image tag on line 25 was missing an alt tag. 
* [lesson.html](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/lesson.html%20W3C%20markup%20-%20ABKS.png) - The validator flagged that my images within the lesson content were missing alt tags.
* [game.html](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/game.html%20W3C%20validator%20-%20AAKS.png) - The validator notified me that I had an empty h1 element on line 62. This is a container for the quiz question. To fix this, I added some placeholder text and then added the hidden class from my CSS and then added some additional Javascript to remove this class when the game is started. The validator also notified me that lines 72 and 78 where I have section tags, I need to have heading elements to correspond. I changed these to div elements to rectify. I also forgot to close my section element on line 59. 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

[style.css](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/CSS%20validator%20-%20AAKS.png) - Hooray - no errors found. 

[Jshint](https://jshint.com/) - There were a few unnecessary semicolons that I removed as per the validator's instruction; however, there were a number of notifications that my code was for Javascript ES6, which is the version that I intended to write my code in, so I don't see a reason to take action from these [notifications](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/Jshint%20-%20AAKS.png). 

## Automated Tests

Automated Tests can be found in game1.test.js within the static, js and test folders. I opted to test three important functions of the game, rather than all of them, as per the project requirements. I wrote the code first and the test cases after, as was recommended to me by my mentor, who believes that this is the right way to learn at my stage of development. Within a professional environment, a test driven development (TDD) approach would be preferable or required. 

I tested that DOM elements were appearing and disappearing as appropriate for my first three functions - startGame, readyQuestion, and newQuestion. I tested this with Jest and by using their [documentation](https://jestjs.io/docs/getting-started). View my test coverage [here](https://github.com/samcat437/Milestone-2/blob/main/docs/Code-Validation/jest-coverage.png).

I struggled with my global let variable "n" while writing test cases. "n" is the variable representing the index for the questions array which changes the questions as they populate the page and the user clicks the next question button. I wrote the test case on line 122 of game1.test.js which tests that once the last question is reached, the next button will disappear and the submit button will appear. The test was not passing with "n" being incremented on line 152 of game1.js. I moved it to the selectAnswer function, but then this caused another test to fail. Moving "n++" to the end of the newQuestion block as well as rewriting the code so that when the second to last question was reached does the code execute solved these issues. Later on I rewrote this again to account for the last question being reached, not the second to last. The test continues to pass and I believe it is fine to include as a test case as it shows the development process.

## Manual Testing 

Manual tests were conducted throughout the development process in order to understand how the DOM was being manipulated. Chrome Dev tools were utilised for the use of the console as well to verify the site's responsiveness and visual presentation. The Github Pages link was tested on several devices including iPhone XR, iPad 2nd Gen, iPad Air 2, HP Envy Laptop, and Macbook Pro. Colleagues at my work also tested it on their various devices and sent me screenshots of issues. Some had Huawei and Android devices. I tested it on Chrome, Edge, Safari and Firefox. 

### Test Cases based on User Stories

#### Home Page

1. As a visiting user, I would like to understand what the purpose of the website is.
    * When first loading the page, the user sees the message on the home page which greets the user and addresses the purpose of the webpage. 
2. As a visiting user, I would like to navigate towards the lessons page and the quiz page.
    * The user sees the lesson and game page buttons which take them to the relevant pages. They can also navigate via the navbar.
[View the home page here](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/home%20AAKS.png)

#### Lesson Page

1. As a visiting user, I would like to view content of the website. 
    * The user can view the lesson content is a scrollable, narrative layout.
    [Lesson Page top](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/lesson-top.png)
2. As a visiting user, I would like to navigate towards the quiz page. 
    * The user is invited to the game page via a button at the bottom of the lesson content. They can also skip to the game page via the navbar.
    [Lesson Page bottom](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/lesson-bottom.png)

#### Game Page

1. As a visiting user, I would like to view the question displayed on page one at a time. 
    * After clicking the start game button, the user is displayed one question. The user knows there will be more questions because there is a next button after checking their answer. [Game Page one question](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/game-next-question.png)
2. As a visiting user, I would like to click on a button to make a response. 
    * The user selects an answer by clicking it. They will know it is selected because it changes colour. [Game Page selection made](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/game-selection.png)
3. As a visiting user, I would like to check my answer.
    * The user checks their answer by clicking on the click answer button. This highlights their selection either in green if correct or red if incorrect. If incorrect, the correct answer is written below the options. [Game Page Check Answer](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/game-answer.png)
4. As a visiting user, I would like to view how many correct answers I had in the score section.   
    * When a user selects an answer correctly, the score counter increments. [Game Page Score](https://github.com/samcat437/Milestone-2/blob/main/docs/test-screenshots/game-score-increment.png)
5. As a visiting user, I would like to navigate back to the home or the lesson page at any time via the navbar.
    * The user can scroll up to access the navbar. I did not make the navbar sticky on this page because the user may have to scroll a bit in order to see the entire game area on their device, and I did not want the navbar to cut off the image or question at any point.

## Deployment 

### Via Heroku 

1. Navigate to the Github repository at [here](https://github.com/samcat437/Milestone-2).
2. Choose "Settings."
3. Click on "Pages."
4. Ensure the main branch and the root directory are selected.
5. Copy and paste the url into the browser or click on the live [link](https://samcat437.github.io/Milestone-2/).

### Via Gitpod

1. Navigate to the Github repository at [here](https://github.com/samcat437/Milestone-3).
2. Choose "Gitpod."
3. In the Bash terminal, type: `set_pg` and then `python3 app.py`
4. Choose "Make Public" when a blue button appears.
5. Choose "Open Browser" when the options appears.

### Acknowledgements

Massive thanks to my Code Institute mentor for guiding me through the development process. Thank you to tutor support for being patient during tutoring sessions. 