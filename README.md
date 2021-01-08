List of Technology Used: JSX, CSS, JavaScript, React, Django, Python, Django REST Framework

Wireframes: https://imgur.com/gallery/lM2bWEk

Entity-Relationship-Diagram: https://imgur.com/gallery/IdfLQ59

Front End Repository: https://github.com/nickromero-prog/meditation-app-react

Front End Deployed Site: https://nickromero-prog.github.io/meditation-app-react/

Back End Repository: https://github.com/nickromero-prog/meditation-app-django

Back End Deployed Site: https://django-deploy-med-app.herokuapp.com/

User Stories:

As a user, I want to be able to sign-up in order to keep track of my meditation sessions.
As a user, I want to be able to sign-in in order to keep track of my meditations sessions.
As a user, I want to be able to choose the length of my meditation session in order to keep to my schedule.
As a user I want to be able to start a timer for my meditation session.
As a user I want to see my meditation sessions in order to see how I have been practicing.
As a user I want to be able to delete a session in case I feel like I don't want that one counted
As a user, I want to be able to restart my session in order to start over or cancel my current session.
As a user, I want to be able to sign-out so that my sessions reflect only me.

Future Problems to Fix:
1) I want to add a timer and a clock so that you can create the sessions
as a user while you're meditating rather than logging a session after you time yourself.
2) I would also like to add more styling and star wars styling to complete that connection.

Strategy:
I wanted to create a meditation application for people to pretend to be jedi and just simply log their sessions in the application so that the user could look back on how well they stuck to their goals or schedule. I began by picking up a React template to get started with and connecting it to my API created with Python and Django Framework. I really wanted to challenge myself to use these technologies since they are relatively new to myself. After that I created 2 routes on my api to handle creating, updating, deleting, and reading my resource (a session). After that I created 3 components within React that handle the CRUD actions of my resource. I then added some styling to connect the jedi user experience. Getting around bugs was simply data transfer problem solving. I utilized console.log() quite a bit to make sure I was sharing data around the project correctly.

API Routes:
## AUTH
| Verb   | URI Pattern        | Controller#Action          |
|:-------|:----------------   |:------------------         |
| POST   | `/sign-up`         | `users#sign-up`            |
| POST   | `/sign-in`         | `users#sign-in`            |
| DELETE | `/sign-out`        | `users#sign-out`           |
| PATCH  | `/change-pw`       | `users#change-password`    |

## PRODUCTS
| Verb   | URI Pattern              | Controller#Action    |
|:-------|:----------------         |:------------------   |
| GET    | `/sessions/`             | `sessions#index`     |
| POST   | `/sessions/`             | `sessions#create`    |
| GET    | `/sessions/:sessionId`   | `sessions#show`      |
| PATCH  | `/sessions/:sessionId`   | `sessions#update`    |
| DELETE | `/sessions/:sessionId`   | `sessions#delete`    |
