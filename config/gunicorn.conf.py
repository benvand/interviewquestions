from django.conf import settings
sitename= settings.SITE_NAME.lower()
bind=["unix:/tmp/gunicorn.%s.sock" % sitename,]
workers=4
accesslog="/var/log/gunicorn.%s.access.log" % sitename
errorlog="/var/log/gunicorn.%s.error.log" % sitename
daemonize=True
