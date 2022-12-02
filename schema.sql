CREATE TABLE Courses (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE, 
    course_id TEXT UNIQUE, 
    description TEXT);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN);

CREATE TABLE Course_registration (
    course_id INTEGER REFERENCES Courses,
    user_id INTEGER REFERENCES Users);

CREATE TABLE Exercises (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES Courses,
    exercise_nr INTEGER, 
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    answer INTEGER);

CREATE TABLE Course_statistics (
    user_id INTEGER REFERENCES Users,
    course_id INTEGER REFERENCES Courses,
    exercise_id INTEGER REFERENCES Exercises,
    completed BOOLEAN);