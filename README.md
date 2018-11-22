# Datatables example

This is an examples of a datatables implementation for a django project.

### Dependencies
- django 2.1.2
- django-braces 1.13.0
- django-filter 2.0.0
- djangorestframework 3.9.0

## Getting Started
First thing is to clone the project into the folder you want to work from.
`git clone https://github.com/dmckim1977/datatables_example.git`

Then we need to create a virtual environment to install the dependencies.
`virtualenv env`

Activate the virtual environment.
For windows run:
`./env/Scripts/activate`

For linux:
`source env/bin/activate`

### Installing
Install the requirements.
`pip install -r requirements.txt`

## Setting up Django
CD into the myproject folder.
`cd myproject`

Run migrate to set up the database.
`python manage.py migrate`

Create a superuser so we can add rows to the database.
`python manage.py createsuperuser`

Run the app.
`python manage.py runserver`

#### Adding the datatables editor trial css and js files
Download the trial css and js files for [Datatables Editor](https://editor.datatables.net/download/).
You will select the option that says JS+CSS. 
Place the `js/dataTables.editor.js` and `js/dataTables.editor.min.js` files in the following folder.
```datatables_example/myproject/static/Editor-2018-01-03-1.7.0```

The trial is good for 15 days. After that you will need to pay to use the editor funtionality.
I added a .gitignore file inside `myproject/static/Editor-2018-01-03-1.7.0`. You will want to remove this when you add your files. 

## Using the app
Go into the admin to create a table so we have something to view. 
`127.0.0.1:8000/admin`

Add a record to the invoices table under the DATATABLES_EXAMPLE app.

Now you can navigate to 127.0.0.1:8000 to view the table.

You can also view the record from the api.
`127.0.0.1:8000/api/unpaid_invoices/`
