## Django CRM

DjangoCRM is an open-source Customer Relationship Management (CRM) system built with Python and the Django web framework. The system is designed to help businesses manage their customers.


## Installation

1. Install Python and Django if you don't have them already. You can download Python from the official website here, and install Django using pip:

```
pip install django
```

2. Clone the repository to your local machine using:

```
git clone https://github.com/jameshunter1/CRM.git
```

3. Navigate to the project directory using the command line.

```
cd django-crm
```

4. Create a virtual environment and activate it using:


`python -m venv env source env/bin/activate `
(for Mac/Linux) 

or 

`python -m venv env source env\Scripts\activate`
(for Windows)`

5. Install the required dependencies using:

```
pip install -r requirements.txt
```

6. Set up the database by running the following commands:

```
python manage.py makemigrations

python manage.py migrate
```

7. Create a superuser account to access the admin panel:

```
python manage.py createsuperuser
```

8. Start the development server using:

```
python manage.py runserver
```

9. Open your web browser and go to http://localhost:8000 to see the CRM app in action.

## Features





## Acknowledgments

This CRM app was built using Django, a high-level Python web framework. We would like to thank the Django community for their contributions to the development of this powerful tool. We also acknowledge the contributions of the open-source community in general, whose efforts have made it possible to create and share software like this.

## Contributions

Contributions to DjangoCRM are always welcome! If you would like to contribute, please follow these steps:

  1. Fork the repository
  2. Create a new branch: git checkout -b my-new-branch
  3. Make your changes and commit them: git commit -am 'Add some feature'
  4. Push your changes to your fork: git push origin my-new-branch
  5. Submit a pull request
  
