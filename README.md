Requirements:

1: Latest python build along with pip
2: Virtualenv (Install via pip install virtualenv)
3: Django

Notes: For Mac users, use pip3 instead of pip and python3 instead of python

How to load this project:

1. Download the repo via zip and save it to your desired location
2. Head into WSD_Project\estore directory and open cmd
3. Create virtual environment via virtualenv env
4. Start the same using .\env\scripts\activate
5. Now install the following things in virtualenv:
   Django (pip install django)
   Pillow (pip install pillow) || for images to load
6. Run application by using the cmd python manage.py runserver or python manage.py runserver port_of_your_choice (eg. python manage.py runserver 9000)
7. When first open we could see that the app is under maintenance. To activate the app, go to http://127.0.0.1:8000/admin/ and enter the following credentials

   Username:rbadv
   Password:password

8.Now return back to the homepage and you are good to go


How to Add/Remove Products:

Add:

1.go to http://127.0.0.1:8000/admin/
2.Select Product Table
3.Select Add new product
4.Fill up the field shown in the page. (Keep the digitalized field untouched)
5.Select save
6.Now return back to the homepage and you can view the changes

Remove:

1.go to http://127.0.0.1:8000/admin/
2.Select Product Table
3.Select the checkbox for your desired product 
4.Go to action and select delete
5.Now return back to the homepage and you can view the changes

Update:

1.go to http://127.0.0.1:8000/admin/
2.Select Product Table
3.Select your desired product 
4.Update the field shown in the page. (Keep the digitalized field untouched)
5.Select save
6.Now return back to the homepage and you can view the changes
