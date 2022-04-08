# DJANGO_CRON_TABBLE_REZERV_DB


 pip install django-dbbackup

 INSTALLED_APPS = (
    ...
    'dbbackup',  # django-dbbackup
)

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

Open Directory buckup

python manage.py dbbackup

python3 manage.py dbrestore

_______________________________________________________________________________________________________________________________________________________________________

pip install django-crontab

INSTALLED_APPS = (
    'django_crontab',
    ...
)

myapp/cron.py:

from django.core.management import call_command

def my_backup():
  try:
      call_command('dbbackup')
  except:
      pass
      
settings.py:

CRONJOBS = [
    ('*/1 * * * *', 'myapp.cron.my_scheduled_job')
]

python3 manage.py crontab add

python manage.py crontab show

python manage.py crontab remove

_____________________________________________________________________________________________________________________________________________________________
