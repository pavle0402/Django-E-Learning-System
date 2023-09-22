<h1>Linden e-learning system</h1>

<h3>Description:</h3> 

Welcome to the E-Learning System App, a comprehensive online learning platform meticulously designed to facilitate and elevate the user's learning journey.
This project represents a unique and innovative approach to e-learning, driven by the aspiration to provide an exceptional educational experience.

This project embodies the spirit of authenticity. It was conceived as a departure from conventional development tutorials.
While external ideas and inspiration played a role, every aspect of this platform was conceived from scratch. The goal was to create something original, innovative, and reflective of a developer's growth journey.
 ---

<h3>Table of Contents:</h3> 

 

Installation 

Features 

Usage 

Configuration 

Security 

Contributing 

License 


 

 

 ---

<h3>Installation:</h3> 

 

To run gym management system, follow these steps: 

 

Clone the repository on your machine: 

 
	git clone https://github.com/pavle0402/Django-E-Learning-System.git

 

Navigate to the project directory: 

cd your-path-to-gymmanagementsystem 

 

3. Create a virtual environment (optional but recommended) and activate it: 

python –m venv venv 

 

 

4. Activate your virtual environment: 

On windows: 

venv/Scripts/activate 

 

On macOS/Linux: 

Source venv/bin/activate 

 

5. Install project dependencies: 
	pip install –r requirements.txt 

 

6. Configure database connections in settings.py. 

 

7. Apply database migrations: 

py manage.py migrate 

 

8. Create superuser(staff) account: 

py manage.py createsuperuser(then you will be asked to provide 	username, email and password) - creating staff user

Or just register as a regular user through the app.

9. Start a development server: 

py manage.py runserver 

 

Application should now be running on: http://localhost:8000. 

 

 
---
<h3>Key Features:</h3> 

- **User Authentication:** Users can register, log in, and log out securely.
- **Homepage:** Explore frequently asked questions (FAQs), top-rated courses, and an app overview.
- **Instructor Profiles:** Discover instructors, their skills, and the courses they teach.
- **Course Listings:** View a list of available courses.
- **Course Details:** Access detailed information about each course, including descriptions, prices, and user ratings.
- **Enrollment:** Users can enroll in courses to access the course content.
- **User Profiles:** Personalized user profiles display profile pictures, social media links, and the courses they have enrolled to.
- **Feedback Section:** Share feedback and ratings for each course.
 

 
 ---

<h3>Screenshots:</h3> 

Admin pov home page:
<img src="screenshots/admin pov/adminhome.png" width=450 height=350>
List of courses:
<img src="screenshots/Screenshot 2023-09-22 121720.png" width=450 height=350>
Course detail example(there is also enroll and feedback section on the same page, as well as reviews of all the users that provided feedback)
<img src="screenshots/Screenshot 2023-09-22 121732.png" width=450 height=350>

 As there are many screenshots for this project, i won't attach them here. You can check all the other pictures in "screenshots/" folder inside this repository.
 ---

<h3>Technologies used</h3> 

- Frontend: HTML, CSS, JavaScript
- Backend: Django
- Database: SQLite(django's default)
- Other technologies and libraries
 

  ---


<h3>Contributing</h3> 

Contributions to the project are welcome! If you would like to contribute, please follow these guidelines: 

Fork the repository. 

Create a new branch for your feature or bug fix. 

Make your changes and commit them with descriptive messages. 

Push your branch to your fork. 

Submit a pull request with a clear explanation of your changes. 

 
 ---

<h3>Creating process:</h3> 
<p1 style="text-align:center;">
**Project Overview**
Welcome to the E-Learning System App, a project born out of a desire to create an original and innovative e-learning platform. Unlike following conventional tutorials, this project was developed from scratch, showcasing my commitment to authentic and creative solutions.

**Challenges and Growth**
While developing this project, I encountered various challenges. One notable challenge was implementing a Celery Beat schedule for managing announcements, which didn't work as expected. However, as a developer committed to continuous growth, I chose not to address this issue at this stage.

**Project Philosophy**
This project evolved into a platform resembling popular e-learning platforms like Coursera or Udemy. The journey began with a vision to create something unique and not just replicate existing tutorials. My goal was to demonstrate originality and my evolving skills as a developer.

By sharing this project, I aim to showcase my ability to take an idea from concept to realization, overcome challenges, and think outside the box in creating functional and innovative solutions.
 </p1>

For any questions or inquiries, contact me at pavles2002@gmail.com 

