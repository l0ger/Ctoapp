file usage
-----------------------------------------------------------------------------
Procfile: used for heroku provider
 heroku use this file for run app. we use gunicorn webserver to run app
 -----------------------------------------------------------------------------
 requirements.txt: this file use by heroku for installing requiring dependency
 also heroku use this file use detect python app
 -----------------------------------------------------------------------------
 runtime.txt:this file use by heroku to install python
 -----------------------------------------------------------------------------
 wsgi.py: the name of this file is important for openshift provider
 openshift provider search in root directory and find wsgi.py then run it.
 ---------------------------------------------------------------------------
