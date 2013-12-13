#!/usr/bin/env python
import os
import sys

sys.path.append('/home/ben')
sys.path.append('/home/ben/interviewquestions')
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interviewquestions.settings")

    from django.core.management import execute_from_command_line

    from django.conf import settings
    if sys.argv[1] == 'collectstatic' and settings.DEV:
        print 'Not on DEV asshole. Staticfilesfinders does it for you'
        raise
    execute_from_command_line(sys.argv)
