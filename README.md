git add .

git commit -m "Test"

git push origin main



Flask CRUD Application – Complete Setup and Lab Notes

1\. Environment Setup

Follow these steps to install and configure the Flask environment:

1\. Step 1: Install virtualenv

 Command:

pip install virtualenv

2\. Step 2: Create and activate virtual environment

 Commands:

python -m venv env

 env\\scripts\\activate # (for Windows)

3\. Step 3: Install Flask and SQLAlchemy

 Command:

pip install Flask Flask-SQLAlchemy

2\. Creating a Flask Application

Step 1: Create a file named app.py in the project directory.

4\. Step 2: Basic Flask app structure:



from flask import Flask

app = Flask(\_\_name\_\_)

@app.route(\&quot;/\&quot;)

def hello\_world():

return \&quot;Hello, World!\&quot;

if \_\_name\_\_ == \&quot;\_\_main\_\_\&quot;:

app.run(debug=True)



5\. Step 3: Run the Flask App

 Command:



python app.py

3\. Templates and Static Folders

6\. Create the following folders in your project directory:

 templates

 static

Ensure they are not created inside the env folder.

4\. Creating HTML Templates

Create index.html inside the templates folder with basic HTML structure:

\&lt;!DOCTYPE html\&gt;

\&lt;html\&gt;

\&lt;head\&gt;

\&lt;title\&gt;Flask App\&lt;/title\&gt;

\&lt;/head\&gt;

\&lt;body\&gt;

\&lt;h1\&gt;Hello from HTML\&lt;/h1\&gt;

\&lt;/body\&gt;

\&lt;/html\&gt;

5\. Beautifying with Bootstrap

Visit https://getbootstrap.com and copy the starter template code into index.html inside

\&lt;head\&gt;.

You can also add forms, navbars, and tables from Bootstrap components.

6\. Setting Up Database with SQLAlchemy

Install SQLAlchemy (already done in step 3):

pip install Flask-SQLAlchemy

Update app.py with database configuration and model definition.

7\. Full Working CRUD App Code

Paste the complete code provided in the lab into app.py.

8\. Creating the Database

Use Python shell to initialize the DB:



python

\&gt;\&gt;\&gt; from app import app, db

\&gt;\&gt;\&gt; app.app\_context().push()



\&gt;\&gt;\&gt; db.create\_all()

\&gt;\&gt;\&gt; exit()



9\. Required Template Files

1\. index.html – To show data and form

2\. update.html – To update records

10\. Running the Application

Command:

python app.py

Visit http://localhost:5000 in your browser.

