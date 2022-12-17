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


   ## Final Deadline Development notes (18.12.2022)
   
   The web application is ready for the purposes of this course. The app is functional both locally and at fly.io. No major changes has been implemented since last deadline as it was mostly complete already back then. Most notably some cyber-security aspects have been dealt with. CFSR-weaknesses have been fixed in all situations of the website. There has been some further improvment into what kind of inputs a user can write into text-fields. Errors are now shown in a better way. The code has also been reviewed and cleaned. Some refactoring has been done as well.
   
   #### The application
   In the application you can view what courses are available without any user account. You can choose to register an account. For testing purposes the option to register as admin has been left in. This would of course be removed in a real case scenario.
   
   In the application a student (normal user) can:
   - View courses available
   - Register for a course
   - Unregister for a course
   - complete exercises
   - view their progression on different courses
   
   In the application an admin can:
   - Create a new course
   - Delete a course
   - Create exercises for a course
   - Edit exercises
   - Delete exercises
   - View registered students
   - View students' progression on courses
   - Everything that a student can do

   #### Some minor problems
   There were some minor problems which I and an instructor of the course tried to fix, but we couldn't. Sometimes when loading the page for the first time there is an emediate error. This is solved by entering "/logout" into the url. Because of this I believe the program may some certain times not properly delete a users session when exiting the website. This however doesn't happen every time and hasn't actually happened now for a couple of weeks so I don't even know if it is still present. 
   
   The other thing was that I got this response in labtool: Älä laita versionhallintaan salaista tietoa, kuten istuntojen salaista avainta tai osoitetta, jonka kautta pääsee käsiksi tuotantotietokantaan. We tried to find this file with the instructor, but to no avail. Please let me know where to find it and how to delete it if it is still there, or was this just some general advice not specifc to me?
      
   #### Final thoughts
   This course has been immensly giving and I have really learned a lot. It has been tons of work with many bugs, but in the end it was always motivating to push further since you were builing something. Thank you for the course and have a great Christmas!
     
   ## Third Deadline Development notes (4.12.2022)
   
   The core structure of the program is ready. The program differs from the original plan on a couple notes. There are no text exercises present. ALl exercises use radiobuttons for answers. An natural addition is that an admin account also has all functions of a normal user. There is a minor bug present which I currently don't know the cause of. Something is fishy about how the progression is programmed or visualized. Needs some reloads to show properly. All other core functionalities have been implemented. 

##### A minor note on the structure:
The architecture follows a basic set up where there is one module of functions per table in the database (users.py, courses.py, course_registration.py, exercises.py and statistics.py). All of these are entirely independant except for statsistics.py. This module also accesses other tables than table: statistics. 

I'm was a bit worried when starting to develop statistics.py on if it would turn out to have too many dependencies, but at the end it worked out fine in my opionion. 

##### Still left to do
   
   1. Fix levels cross UI.
   2. Apply cyber-security.
   3. Code reviewing. (Light refactoring and renaming if need be).
    
   If time allows:
   
   4. Customize UI.
   5. Testing. (I haven't read anywhere that this should have been part of the course?? Please tell me if it is in the response.)
   6. More functionalities.

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
    
   

