# About
- This project uses network(Project 4) as starting template 
- This project provides a template to design a personal website to showcase and share projects, resume with others
- Login is required to edit users own profile, projects and there should be  no add or remove button both in front end and server side check
- Should be able to publicly viewed by anyone  in case of no login
- Bootstrap is used for mobile responsive site. Auto adjust forms according to screen size width etc
- Uses 3 models:user,profile,skills on backend and some javascript fuctions on front end
- Most of the functions are limited because of time constraigns. Infuture there is a possiblity of adding certificates, colors better style design, contact information etc for better website


# Distinctinvness
- This is a personal website template designer similar to a blog where you can share your profile and projects
- This is distinctive from social network where the main goal is the posts,followers etc while this project focuses on good template design to showcase all your work as a form of blog
- This blog or personal website provides a means of communication to employeers, potential recuriters etc with more flexibility regarding what you want

# Complexity
- The complexity mostly compromises of design,logic to add, edit, share users profile,projects. 
- While this project employs basic priniciples the main goal is to satisfy the requirments(1 model, js,mobile responsive,488 words:500 neighborhood,distinictive and complexity) and complete capstone as simple as possible with limited time available


# Files
- models.py contains Profile,Skills, User Models
- certificates model is not employed due to time constrains
- Profile table stores title,description and dates
- Skills table stores skills of particular user
- User table stores user details
- views.py contains /login and /logout functions respectively
- profile and projects html contains template for each user resume,projects to be displayed
- views.py also contains add_entiy,delete,add_skills code respectively. 
- can share profile(profile method in views.py)) with profile/username and profile/username/projects(projects method) cannot add or edit without login. 


# Instructions to Run
- Default (/) takes to login.
- /register to register or /login to login it redirects to / (index function)
- index function if logged in goes to /profile/username
- Nav bar contains projects which redirects to /profile/username/projects
- profile and projects get data from Profile Table containing entiy,dates,description to be displayed
- Add button can be used to display form and submit data to add_entity route. This will add to profile table(table-entity,date,description)
- Delete will delete data from Profile Table
- Add button under skills will update or add existing skills
- Security of profile name and the userlogged in is matched backend apart from frontend implementation before adding, or deleting anything within database
- Csrf token also used for cross site prevention
- No form checking is employed giving the user freedom/flexibility for empty etc
- python mange.py makemigrations network, python mange.py migrations and python mange.py runserver to test, hello is super user with same password for testing added to this readme

# Video
- default route always takes to login.
- default route if logged in redirects to profile to add any rows
- /profile/username to share and /profile/username/projects for projects
- add, delete  and update skills explained

