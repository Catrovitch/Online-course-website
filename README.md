# Online-course-website

#### Background

This online-course-website will be developed as a project for the course Tietokanta Sovellus at University of Helsinki. The idea of the course is to build a project that focuses on website development that makes use of databases. I will use the PostgreSQL database management system and Python's Flask library to build the project. In the course material for the course Tietokanta Sovellus there where some proposed example subjects and I have chosen to focus my project on the proposed subject of a website for online courses. I have chosen to do this subject since I have very limited experience in web development and choosing this subject seemed like a solid choice for me to develop a project while at the same time learning about webdevelopment. The course Tietokanta Sovellus is worth 4 study points. Here is a link to the University of Helsinki course webpage: [Tietokanta Sovellus](https://hy-tsoha.github.io/materiaali/).

## Description of Program

I will be developing an online-course-website which can be used to set up various online courses. The program will contain both text based material and exercises of various nature. All users will be either a teacher (administrator) or a student (normal user). 

##### Some functionalities of the program:

- A student can: 
  - Create an account of student status.
  - Log in to the service.
  - See what courses are available.
  - Apply for a course.
  - Read the course material.
  - Do course exercises.
  - Review statistics about course progression.

- A teacher can:
  - Create a new course.
  - Change course material.
  - Delete a course.
  - Add more exercises to a course.
  - Track what student is on what course, as well as their progression.
 
##### Exercises

The exercises will consist of automatically checked exercises that are either text based or multiple-choice-questions. 
  
  - A text based question could be:
    - How many legs does an insect have? (give your answer in non-capital letters)
      - Here would be a text field where the student can answer.
      - The answer will then be compared to the correct answer: "six".
      
  - A multiple-choice-question could be:
    - Choose the correct alternative:
      - An insect has eight legs
      - An insect has two-and-a-half leg
      - An insect has six legs
      
     - Comment: There would be a checkboxed at the right side of each alternative choice.
     
   ## Second Deadline Development notes (20.11.2022)
   
  During this week I have implemented fly.io functionality and started developing the core functionalities of the service. Due to my limited experience with any sort of web development I struggled quite hard to figure certain things out. At the end I think I learned a lot and fell much more confident for future assignments. 
  
  - Backend:
      - A fucntioning main application both locally and through fly.io
      - Schema.sql
      - A functioning database which includes atleast a preliminary structure.
        - Tables: Users, Courses, Course_registration, Exercises and Course_statistsics (All are not in use yet).
      - A functioning main application.
      - routes for index, login (this will probably be deleted in the future), courses, logout, register, register_admin (for development purposes only) and admin.
      - A user can register an account.
      - A user can log in with his/her credentials.
      - A user can view available courses.
      - Admin page where an admin can view available courses and students.
      - Admin can create a course
      - Admin can delete a course
      - Admin module (This didn't work for some reason. This will probably be deleted in the future, as it was anyways developed for development reasons only).
  - Frontend:
    - index.html which funcitons as a main page. Uses Bootstrap. Will be improved upon in the future.
    - Rest of the frontend is at a very early stage, but there are functioning pages for admin.html, courses.html, error.html, login.html (will be deleted), register.html.
    - register.html includes the option to create an admin account. This is for development reasons purely.
    
### Launch app:

To visit the webpage click [here](https://online-course-website.fly.dev/)

To test the application locally you first need to clone the repository with command:
```
git clone git@github.com:Catrovitch/Online-course-website.git
```

Activate virtual environment with command:
```
source venv/bin/activate
```

Then install dependencies with command:
```
pip install -r requirements.txt
```

Now you can launch the app locally through the command "flask run". For this to work you need to remove ".replace("://", "ql://", 1)" from line "app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)" in file db.py. This is due to some error not completely clear to me at the moment.

Launch app locally:
```
flask run
```

Good luck!

