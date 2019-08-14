## Django Rename Project

1. Rename your **project directory** (ProjectName) and the following inside your project directory.

2. settings.py

   ```python
   ROOT_URLCONF = 'NewProjectName.urls'
   WSGI_APPLICATION = 'NewProjectName.wsgi.application'
   ```

3. wsgi.py

   ```python
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewProjectName.settings")
   ```

4. manage.py

   ```python
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewProjectName.settings")
   ```

   

