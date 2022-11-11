CREATE TABLE Courses (id SERIAL PRIMARY KEY, name TEXT, course_id INTEGER, description TEXT);
CREATE TABLE USERS (id SERIAL PRIMARY KEY, username TEXT, password TEXT, admin BOOLEAN);
