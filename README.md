How to run and use our project: 
	-in terminal, navigate to directory containing manage.py
	-run a command to start the server with some port number 
		e.g. python manage.py runserver 0.0.0.0:8127
	-to access app from web browser, go to http://dutch.mathcs.emory.edu:8127
	-app is straightforward, just click buttons with mouse.

inner workings of our project:
	-html is used for layout and design of the app page
	-each button submits a form and is processed by django views
	-django views can return some variables which are updated in the webpage
	-calculator input/result/memory are stored in database

team member contributions:
	Austin Dong: python & django programming/debugging, initial html layout
	Zeyu Zhang: advanced html layout and design, debugging
