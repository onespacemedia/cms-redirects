django-redirects
================

Allow admin users to add redirects from one path to another. At the moment it's just an application which you would copy into your project, but in the future it may change into an installable module.

To use django-redirects simply add the apps/redirects folder into your apps folder and update your settings file with the 2 lines shown in settings/production.py. Once the application is in place and the settings files have been modified you will need to run ./manage.py migrate (if you're using South).
