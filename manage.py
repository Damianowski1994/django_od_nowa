#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# #!/usr/bin/env python
# import os
# import sys

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "management.settings")

#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'od_nowa.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver

        # runserver.default_port = os.environ.PORT | "8000"
        print("test --------------  ", os.environ)
        try:
            runserver.default_port = os.environ.PORT
        except:
            runserver.default_port = "8000"
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
