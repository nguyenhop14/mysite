=====
User
=====

UserAuth is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "user_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'user_auth',
    ]

2. Include the user_auth URLconf in your project urls.py like this::

    path('user_auth/', include('user_auth.urls')),

3. Run ``python manage.py migrate`` to create the user_auth models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/user_auth/ to participate in the user_auth.