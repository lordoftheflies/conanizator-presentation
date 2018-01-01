=====
Presentation
=====

Presnetation is a simple Django app to introduce a Polymer 2.0 based progessive frontend.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "conanizator_presentation" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dopamin_presentation',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('presentation/', include('dopamin_presentation.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/presentation/ to participate in the poll.
