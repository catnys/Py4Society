# `Day 71 - Advanced`

# WSGI 
You might recall that every time we ran our app, we got a warning telling us that when we want to make our website go live and go from development to production mode that we should use a WSGI server.

WSGI stands for Web Server Gateway Interface and it's described here: https://www.python.org/dev/peps/pep-3333/

In summary: normal web servers can't run Python applications, so a special type of server was created (WSGI) to run our Flask app.  Essentially, a WSGI server standardises the language and protocols between our Python Flask application and the host server.

There are many WSGIs to choose from, but we'll use the most popular - gunicorn. That way our hosting provider will call gunicorn to run our code.

Add gunicorn to the requirements.txt


1. Check if you have the gunicorn package included in your requirements.txt. If you are using the starting code for this section, you should see it listed. If you are using your own code, add gunicorn==21.2.0 to your requirements.txt.
The format for all the packages in the requirements.txt is:

gunicorn==<version number>



2. Next, we need to tell our hosting provider about our gunicorn server, what our app is called, and how to run our Flask app. We do that using a config file called a Procfile.



## Create a Procfile


3. Create a new file in the project top-level folder called Procfile. When you create the new file, PyCharm will prompt you to track the new file under git version control. Agree by clicking add.

NOTE: make sure you spell the name of the file exactly as you see above, with a capital P and no file extension.

Type the following into the Procfile:



web: gunicorn main:app


This will tell our hosting provider to create a web worker that is able to receive HTTP requests. The Procfile also says to use gunicorn to serve your web app. And finally it specifies the Flask app object is the main.py file. That way the hosting provider knows about the entry point for the app and what our app is called.

