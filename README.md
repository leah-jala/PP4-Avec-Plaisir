# AVEC PLAISIR

"Avec Plaisir" (With Pleasure) is a fictional French Restaurant located on Charlotte Street in London, which is a wonderful location for food lovers to enjoy food from independent restaurant owners.

The webpage was created as a restaurant management application to allow the site owner, with staff, to present their restaurant to the works and

- Take and manage bookings
- Manage menus
- Allow customers to make and manage their own bookings. 


## Table of Contents
* [Website Design](#website-design)
    * [The Strategy Plane](#the-strategy-plane)
    * [The Scope Plane](#the-scope-plane)
        * [Agile Planning](#agile-planning)
    * [The Skeleton Plan](#skeleton-plane)
        * [Wireframes](#wireframes)
        * [Database Design](#database-design)
    * [The Surface Plane](#surface-plane)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## WEBSITE DESIGN

(REFERENCE USED - CI User Experience Essentials, "It's all about the user experience)

### The strategy plane

#### Goals

Why is the site needed? This is a website for a restaurant. The goals are to 
1. Make the restaurant look attractive.
2. Allow customers to view the menus.
3. Allow customers to make and manage a reservation.
4. Allow staff to easily make and manage their own bookings, menus and users.

#### Emotional factors

If the website looks attractive and runs efficiently, using few clicks and showing responsiveness, it is a good reflection of the restaurant's customer care and attention to detail as an overall part of the product they deliver ot customers, including the eventual food. 

#### Target Audience

The website needs to cater to  site owner, restaurant staff and customer needs.

- Site owner and Staff:
    - Where do they go first? 
        - The site owner will likely to the the admin panel first, where they can review bookings and made any edits to their menus.
    - What do you use it most for?
        - To view bookings to manage tables when customers arrive without bookings or call on the telephone and manage as appropriate.
        - To CRUD customer bookings if they call in and ask for this. 
        - To keep the restaurant menus up to date. 
    - What happens before/after using the site
        - Before:Staff most likely receive a phone call.
        - Before: Staff need to consult the bookings table to see if they can accommdate a walk-in customer.
        - After: staff members can let the kitchen know how busy the restaurant will be. 

- Customers:
    - Where do you go first?
        - The homepage as it is the main page.
    - What do you use it most for?
        - To look at the menu so I can decide if I feel like eating there.
    - What happens before/after using the site
        - Before: I've search for French restaurants in the area.
        - After: If the website is appealing and I made a booking, I'll tell my friends about it.

What are the most important features? What trade offs are needed



### The Scope Plane

Looking at the goals and use cases above, the following requirements were identified.

- Minimum requirements:
    - There must be a way to take and manage customer bookings with full CRUD.
    - The customer must be able to view the menus.
    - The customer must have information about the location of the restaurant.

- If time permits, or for future development
    - A separate contact page.
    - Email confirmations and calendar syncs.
    - Automation to delete bookings when there are no-shows.
    - Ability to edit menu items from the admin panel.

Constraints:

The main constraint is time. The project is being completed by a sole individual over 4 weeks with the Christmas holidays in the middle.


#### Agile Planning

##### Sprint 1 - 

##### Sprint 2 - 

##### Sprint 3

##### Sprint 4


### Structure Plane
#### Features/User Stories


### Skeleton Plane

#### Wireframes

Wireframes were created to envisage how user can interact with the website in order to 

- simple interaction (not too many clicks, and only include necessary features)
- allow the customer to get an overall feel for the restaurant as quickly as possible.
- allow customer to review opening hours. 
- allow customer to see restaurant location, contact information and social media links.
- allow the customer to make a booking quickly.
- to allow staff to easily review bookings.
- to allow the staff user and designated staff to manage users and permissions.

 
 ##### Homepage
 ![homepage](docs/wireframes/homepage.JPG)

 ##### Menu landing page, and service menus 
 ![menus](docs/wireframes/menu-page.JPG)
 ![individual menus](docs/wireframes/menus.JPG)

 ##### Booking Form
 ![booking form](docs/wireframes/bookings.JPG)
 
 
 ##### Booking Success

#### Database Design



### Surface Plane

#### Design

#### Colour Palette
#### Fonts
#### Images
## Technologies
- Balsamiq Wireframes
- Photo converter: https://cloudconvert.com/jpg-to-webp
- Favicon generator: https://favicon.io/favicon-generator/

## Testing and bugs

## HTML validator 
## CSS validator
## Python validator
## JS validator


### Bugs
- Phone field:  My phone number field was originally too restrictive and only would accept US number. 
 tried different solutions, but ran out of time. For example, I tried to add a country code drop down, and 
 I can see it is possible to default it to a specific country code, but that didn't work for me. I tried to 
 handle the exception so that users could be given advice on how to enter a number correctly, as it did automatically
 by Django, but this wasn't working either. I opted to make it a charfield and not required. As the user has to be 
 signed in to make a reservation, it would still be possible for the restaurant to get in touch about the booking. 
 It is not ideal and it is something I would fix later. 
- myReservations.html - The header in the form used the users first_name, but you are not required to enter a first name when you sign up. I added a fiter to the html so that it would use the first name if it is there and otherwise use the username.

### Create an account

### CreateReservationView Tests
- The user can access the view and see the reservation form
    True - manually tested
- The form is valid and can create a new reservation
    True - reservations are posted to the datbase.
- The form is invalid and doesn't create a new reservation
    True - The form will not submit until all required fields have valid entries. 
- The view redirects to the correct URL after a reservation is made
    True - After the form submits, the user is directed to "My Reservations" where they can see the new entry.
- A success message is displayed after a reservation is made
    True - The message is show at the top of the "My Reservations"" page.



## Deployment

### Early Deployment

This project was deployed as part of the project set up, as advised in the "I think therefore I blog" walkthrough. This is to ensure that our main dependenices are installed and working from the outset. From there one can build the project on a solid foundation and reduce stress at the end of the project. 

The app was deployed with Heroku, ElepantSQL and Cloudinary

#### Project set-up and deployment steps

Install Django and supporting  libraries
- Install Django
- Install Cloudinary
- Create requirements
- Create project, "avec plaisir"
- Create "home" app
- Add home app to installed settings
- Migrate changes to the DB and confirm success
- Add project to the settings
- Migrate to the database
- Run http server to check if the installation was successful

Connect to Heroku and ElephantSQL
- Create Heroku App
- Create new instance on Elephant SQL and copy DB url
- Create env.py, adding the secret key. Ensure env.py is in gitignore
- Import env.py into Settings, and edit secret key accordingly
- Comment out original databases in Settings
- Connect to ElephantSQL
- Make migrations
- Test connect to ElephantSQL was successful
- Add config vars to Heroku

Connect to Cloudinary
- Add Cloudinary API environment variable to env.py
- Add Cloudinary API environment variable to Heroku Config Vars
- Add DISABLE_COLLECTSTATIC to Heroku config vars
- In Settings,  "Installed Apps", add cloudinary_storage and cloudinary

Set up Directories and deploy
- In Settings, under STATIC_URL add STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage', and add STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE
- Add Templates Directory under BASE_DIR in settings, and fill in brackets for "DIR": []
- Add Heroku host name to ALLOWED_HOSTS
- Add top level directories
- Add a procfile
- In Heroku, link to GitHub as the deployment method

#### Final deployment

- In settings, 
    - Set DEBUG to False. If this is not done, cloudinary images won't be served and traceback error messages will be shown to the user (which can also reveal credentials that can benefit hackers).
    - Add X_FRAME_OPTIONS = 'SAMEORIGIN'
    
## Credits and Sources
- Project planning and planes - Reviewed relevant CI lectures and and reviewed a tutorial led by Daisy McGirr on Agile Planning. I also referred to Gareth McGirr's github project/agile planning.
- Deployment steps - These were taken directly from the "I think therefore I blog" walkthrough.
- Datepicker - https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
- Photos from Pexels.com
    - Wine bottles: Stanislav Kondratiev
- Built-in template flags and filters https://docs.djangoproject.com/en/4.1/ref/templates/builtins/


## Sources for future
- Django allauth social login - https://django-allauth.readthedocs.io/en/latest/providers.html#google
