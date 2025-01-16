#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clgproject.settings')
>>>>>>> 1cd9d07 (Initial commit)
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pro.settings')
>>>>>>> 8fd2ff2 (initial commit)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 1cd9d07 (Initial commit)
=======
if __name__ == '__main__':
>>>>>>> 8fd2ff2 (initial commit)
    main()
